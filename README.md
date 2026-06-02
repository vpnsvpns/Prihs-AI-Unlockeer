<h1 align="center">Prihs AI Unlocker</h1>
<p align="center">
  Форк <b>Goida AI Unlocker</b> — мини-утилита для Windows, позволяющая <b>в один клик разблокировать популярные сервисы</b> путём обновления файла <code>hosts</code>. Использует hosts-файлы от <b>GeoHide DNS</b>.
</p>

---

## 🧩 Как это работает
Приложение скачивает свежий файл <code>hosts</code> из репозитория <a href="https://github.com/Internet-Helper/GeoHideDNS">GeoHideDNS</a> и заменяет системный <code>C:\Windows\System32\drivers\etc\hosts</code>. При необходимости предыдущая версия автоматически сохраняется и может быть восстановлена.

---

## 🛠️ Сборка EXE

**Windows:**
```
pyinstaller main.py --onefile --noconsole --icon=icon.ico --clean --strip --name="Prihs_AI_Unlocker_Windows" --noupx --clean --version-file=version.txt --add-data "icon.ico;." --add-data "app_info.json;." --add-data "icons;icons" --add-data "app;app"
```

---

## 📜 Лицензия
GPL-3.0
