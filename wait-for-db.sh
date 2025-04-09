#!/bin/sh

echo "⏳ Esperando o banco ficar disponível em db:5432..."

while ! nc -z db 5432; do
  sleep 1
done

echo "✅ Banco de dados pronto. Iniciando a API..."
exec "$@"
