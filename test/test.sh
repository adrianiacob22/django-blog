sleep 20
if curl http://djangoproject:8000 | grep -i 'Adrian'; then
  echo "Tests passed!" > testresult
  exit 0
else
  echo "Tests failed!" > testresult
  exit 1
fi
