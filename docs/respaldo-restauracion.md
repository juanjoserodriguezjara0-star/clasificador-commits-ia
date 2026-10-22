# Procedimiento de respaldo y restauración de PostgreSQL

Procedimiento para desarrollo local con Docker Compose. Ejecútalo desde la raíz del repositorio. No publiques archivos de respaldo porque pueden contener mensajes de commit.

## Crear respaldo

En PowerShell:

```powershell
New-Item -ItemType Directory -Force backups | Out-Null
docker compose exec -T db pg_dump -U clasificador -d clasificador -Fc -f /tmp/clasificador.dump
docker compose cp db:/tmp/clasificador.dump ./backups/clasificador.dump
```

En Linux o WSL2:

```bash
mkdir -p backups
docker compose exec -T db pg_dump -U clasificador -d clasificador -Fc > backups/clasificador.dump
```

## Restaurar en una base de prueba

No sobrescribas la base original para probar una restauración. Crea una base temporal:

```bash
docker compose exec db createdb -U clasificador clasificador_restore_test
docker compose cp ./backups/clasificador.dump db:/tmp/clasificador.dump
docker compose exec db pg_restore -U clasificador -d clasificador_restore_test --clean --if-exists /tmp/clasificador.dump
docker compose exec db psql -U clasificador -d clasificador_restore_test -c "SELECT count(*) FROM inferencias;"
```

## Evidencia requerida

Registra fecha, comandos ejecutados, resultado de `pg_dump`, resultado de `pg_restore` y conteo obtenido. Este documento describe el procedimiento; marca la prueba como aprobada solo después de ejecutarla en tu equipo.
