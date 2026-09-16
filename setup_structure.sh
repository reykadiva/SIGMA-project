#!/usr/bin/env bash
# Jalankan dari root folder repo SIGMA-project (setelah git clone)
# Bikin skeleton struktur final + .gitkeep biar folder kosong ikut ke-commit
set -e

dirs=(
  "backend/app/api"
  "backend/app/core"
  "backend/app/models"
  "backend/app/schemas"
  "backend/app/services/scoring"
  "backend/app/services/rag"
  "backend/app/workers"
  "backend/alembic"
  "backend/tests"
  "scanner/dorking"
  "scanner/portscan"
  "scanner/fingerprint"
  "scanner/recon"
  "scanner/screenshots"
  "frontend/src/app"
  "frontend/src/components"
  "frontend/src/features/dashboard"
  "frontend/src/features/public-portal"
  "frontend/src/features/auth"
  "frontend/src/lib"
  "frontend/src/styles"
  "frontend/public"
  "docs/sop"
)

for d in "${dirs[@]}"; do
  mkdir -p "$d"
  touch "$d/.gitkeep"
done

echo "Struktur folder final SIGMA berhasil dibuat."
echo "Cek dengan: git status"
