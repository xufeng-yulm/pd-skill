#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

clone_sparse() {
  local repo="$1"
  local dest="$2"
  shift 2
  git clone --depth 1 --filter=blob:none --sparse "$repo" "$dest" >/dev/null 2>&1
  git -C "$dest" sparse-checkout set "$@" >/dev/null
}

mkdir -p "$ROOT_DIR/subskills"

clone_sparse "https://github.com/obra/superpowers.git" "$TMP_DIR/obra" \
  "skills/brainstorming"
rm -rf "$ROOT_DIR/subskills/brainstorming"
cp -R "$TMP_DIR/obra/skills/brainstorming" "$ROOT_DIR/subskills/brainstorming"

clone_sparse "https://github.com/anthropics/skills.git" "$TMP_DIR/anthropic" \
  "skills/frontend-design"
rm -rf "$ROOT_DIR/subskills/frontend-design"
cp -R "$TMP_DIR/anthropic/skills/frontend-design" "$ROOT_DIR/subskills/frontend-design"

clone_sparse "https://github.com/product-on-purpose/pm-skills.git" "$TMP_DIR/pm" \
  "skills/deliver-prd" \
  "skills/utility-mermaid-diagrams" \
  "skills/utility-slideshow-creator"
rm -rf "$ROOT_DIR/subskills/deliver-prd" \
  "$ROOT_DIR/subskills/utility-mermaid-diagrams" \
  "$ROOT_DIR/subskills/utility-slideshow-creator"
cp -R "$TMP_DIR/pm/skills/deliver-prd" "$ROOT_DIR/subskills/deliver-prd"
cp -R "$TMP_DIR/pm/skills/utility-mermaid-diagrams" "$ROOT_DIR/subskills/utility-mermaid-diagrams"
cp -R "$TMP_DIR/pm/skills/utility-slideshow-creator" "$ROOT_DIR/subskills/utility-slideshow-creator"

echo "Vendored subskills refreshed under $ROOT_DIR/subskills"
