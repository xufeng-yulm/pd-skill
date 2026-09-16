"""在临时目录验证初始化行为，避免修改真实案例或调用外部服务。"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/init_pm_case.py"


class InitPmCaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.workspace = Path(self.temp.name).resolve()
        self.root = self.workspace / ".pd"

    def run_init(self, *args, expected=0):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            cwd=self.workspace,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, expected, result.stderr)
        return result

    def read_manifest(self):
        return json.loads((self.root / "feishu/manifest.json").read_text())

    def snapshot(self):
        return {
            str(path.relative_to(self.root)): path.read_bytes()
            for path in self.root.rglob("*")
            if path.is_file()
        }

    def test_standard_manifest_contains_only_all_19_prds(self):
        result = self.run_init("--title", "报销系统")
        self.assertEqual(Path(result.stdout.strip()), self.root)
        manifest = self.read_manifest()
        paths = [Path(doc["path"]) for doc in manifest["documents"]]
        self.assertEqual(len(paths), 19)
        self.assertEqual(len(set(paths)), 19)
        self.assertEqual(
            [path.name[:2] for path in paths],
            [f"{number:02d}" for number in range(19)],
        )
        self.assertEqual(set(paths), set((self.root / "prd").glob("*.md")))
        self.assertTrue(all(path.is_absolute() and path.is_file() for path in paths))
        self.assertEqual(manifest["profile"], "standard")

    def test_lean_has_one_prd_and_no_optional_scaffolds(self):
        self.run_init("--title", "批量导出", "--profile", "lean")
        manifest = self.read_manifest()
        self.assertEqual(manifest["profile"], "lean")
        self.assertEqual(len(manifest["documents"]), 1)
        self.assertEqual(
            Path(manifest["documents"][0]["path"]),
            self.root / "prd/01-feature-spec.md",
        )
        self.assertEqual(len(list((self.root / "analysis").glob("*.md"))), 4)
        for name in ("prototype", "deck", "ops", "diagrams"):
            self.assertFalse((self.root / name).exists())

    def test_nested_chinese_slug_and_custom_base_are_resolved_from_cwd(self):
        result = self.run_init(
            "--title", "订单 退款", "--nested", "--base-dir", "output/cases"
        )
        root = self.workspace / "output/cases/订单-退款"
        self.assertEqual(Path(result.stdout.strip()), root)
        self.assertTrue((root / "prd/00-business-blueprint.md").is_file())
        self.assertFalse(self.root.exists())

    def test_rerun_preserves_edits_and_manifest_but_restores_missing_file(self):
        self.run_init("--title", "报销系统")
        document = self.root / "prd/07-functional-requirements.md"
        document.write_text("# 人工评审结果\n\n请保留。\n", encoding="utf-8")
        manifest_path = self.root / "feishu/manifest.json"
        manifest = self.read_manifest()
        manifest["documents"] = manifest["documents"][2:5]
        manifest["remote_node"] = "preserve-test-value"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        missing = self.root / "analysis/03-evidence-ledger.md"
        missing.unlink()
        before = self.snapshot()
        self.run_init("--title", "报销系统")
        after = self.snapshot()
        for name, content in before.items():
            self.assertEqual(after[name], content, name)
        self.assertTrue(missing.is_file())

    def test_legacy_manifest_is_preserved(self):
        self.run_init("--title", "报销系统")
        path = self.root / "feishu/manifest.json"
        manifest = self.read_manifest()
        manifest.pop("profile")
        path.write_text(json.dumps(manifest), encoding="utf-8")
        before = self.snapshot()
        self.run_init("--title", "报销系统")
        self.assertEqual(self.snapshot(), before)

    def test_conflicting_title_or_profile_fails_before_mutation(self):
        self.run_init("--title", "报销系统")
        before = self.snapshot()
        for args in (
            ("--title", "另一个项目"),
            ("--title", "报销系统", "--profile", "lean"),
        ):
            with self.subTest(args=args):
                self.run_init(*args, expected=2)
                self.assertEqual(self.snapshot(), before)

    def test_invalid_slug_cannot_escape_output_directory(self):
        for slug in ("../escape", "/tmp/escape", "..", "a/b", "a\\b", ""):
            with self.subTest(slug=slug):
                self.run_init(
                    "--title", "测试", "--slug", slug, "--nested", expected=2
                )
                self.assertFalse(self.root.exists())

    def test_empty_or_multiline_title_is_rejected(self):
        for title in ("", "  ", "项目\n伪造标题", "项目\t名称"):
            with self.subTest(title=title):
                self.run_init("--title", title, expected=2)
                self.assertFalse(self.root.exists())

    def test_invalid_manifest_is_reported_without_mutation(self):
        path = self.root / "feishu/manifest.json"
        path.parent.mkdir(parents=True)
        for invalid in ("{broken", "[]"):
            with self.subTest(invalid=invalid):
                path.write_text(invalid)
                result = self.run_init("--title", "测试", expected=2)
                self.assertIn("manifest.json", result.stderr)
                self.assertNotIn("Traceback", result.stderr)
                self.assertEqual(self.snapshot(), {"feishu/manifest.json": invalid.encode()})

    def test_symlinked_artifact_directory_cannot_write_outside_case(self):
        outside = self.workspace / "outside"
        outside.mkdir()
        self.root.mkdir()
        (self.root / "prd").symlink_to(outside, target_is_directory=True)
        self.run_init("--title", "测试", expected=2)
        self.assertEqual(list(outside.iterdir()), [])
        self.assertFalse((self.root / "brief").exists())


if __name__ == "__main__":
    unittest.main()
