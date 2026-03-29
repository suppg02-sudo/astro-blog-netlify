#!/bin/bash
set -euo pipefail

SRC="/media/docker/astro-blog/src"
DST="/media/docker/astro-blog-netlify/src"

echo "=== Sync Theme: Copying from server blog to Netlify repo ==="

for dir in components layouts assets styles utils; do
  echo "Syncing $dir/"
  rm -rf "$DST/$dir"
  cp -r "$SRC/$dir" "$DST/$dir"
done

for file in types.ts env.d.ts; do
  echo "Syncing $file"
  cp "$SRC/$file" "$DST/$file"
done

echo "Syncing content schemas..."
cp "$SRC/content/_schemas.ts" "$DST/content/_schemas.ts"

echo "Syncing content.config.ts..."
cp "$SRC/content.config.ts" "$DST/content.config.ts"

echo ""
echo "=== Done. Review changes and commit manually. ==="
echo "cd $DST/../ && git diff"
