#!/usr/bin/env python3
"""Interactive Onboarding and Setup Wizard for Excalibur BLOG."""

from __future__ import annotations

import re
import sys
from pathlib import Path

def project_root() -> Path:
    return Path(__file__).resolve().parents[1]

def clear_screen() -> None:
    # Print clean separators
    print("\n" + "="*60 + "\n")

def get_input(prompt: str, default: str = "") -> str:
    prompt_str = f"{prompt} [{default}]: " if default else f"{prompt}: "
    try:
        val = input(prompt_str).strip()
        return val if val else default
    except (KeyboardInterrupt, EOFError):
        print("\n\nНастройка прервана пользователем.")
        sys.exit(1)

def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    clear_screen()
    print("""
 ███████╗██╗  ██╗ ██████╗ █████╗ ██╗     ██╗██████╗ ██╗   ██╗██████╗ 
 ██╔════╝╚██╗██╔╝██╔════╝██╔══██╗██║     ██║██╔══██╗██║   ██║██╔══██╗
 █████╗   ╚███╔╝ ██║     ███████║██║     ██║██████╔╝██║   ██║██████╔╝
 ██╔══╝   ██╔██╗ ██║     ██╔══██║██║     ██║██╔══██╗██║   ██║██╔══██╗
 ███████╗██╔╝ ██╗╚██████╗██║  ██║███████╗██║██████╔╝╚██████╔╝██████╔╝
 ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═════╝  ╚═════╝ ╚═════╝ 
    """)
    print("Приветствуем в мастере первоначальной настройки Excalibur BLOG! 🚀")
    print("Этот интерактивный помощник настроит окружение, бриф бизнеса и доступы к сайту.")
    print("Все данные будут сохранены локально и защищены через .gitignore.")
    print("="*60 + "\n")

    root = project_root()
    brief_path = root / "memory/brief/site-brief.md"
    env_path = root / "memory/site.env.local"
    env_example_path = root / "memory/site.env.local.example"

    # -------------------------------------------------------------------------
    # ШАГ 1: Информация о бизнесе и сайте
    # -------------------------------------------------------------------------
    print("--- ШАГ 1: ИНФОРМАЦИЯ О САЙТЕ И БИЗНЕСЕ ---")
    site_name = get_input("Введите название вашего блога/сайта", "Авто-Сейлс")
    site_url = get_input("Введите полный URL сайта (с https://)", "https://avtosales125.ru")
    blog_path = get_input("Укажите путь к блогу на сайте", "/")
    niche = get_input("Какая у вас ниша? (например: SaaS автоматизация, EdTech, b2b услуги)", "авто из Японии, Кореи и Китая под ключ")
    audience = get_input(
        "Опишите целевую аудиторию (простым языком)", 
        "покупатели авто с пробегом из Азии, Владивосток и регионы РФ"
    )
    
    # -------------------------------------------------------------------------
    # ШАГ 2: Доступы к серверу и WordPress (SSH)
    # -------------------------------------------------------------------------
    print("\n--- ШАГ 2: НАСТРОЙКА ИНТЕГРАЦИИ И ИМПОРТА В WORDPRESS (SSH) ---")
    print("Для публикации статей напрямую в вашу WP-тему, укажите данные SSH-сервера.")
    ssh_host = get_input("SSH хост (например: djinoum7.beget.tech)", "djinoum7.beget.tech")
    ssh_port = get_input("SSH порт", "22")
    ssh_user = get_input("SSH пользователь", "")
    ssh_pass = get_input("SSH пароль", "")
    ssh_root = get_input(
        "SSH путь к корню WordPress (где wp-load.php)",
        "/avtosales125/public_html",
    )
    
    allow_publish_input = get_input("Разрешить автоматическую публикацию на боевой сайт? (yes/no)", "no")
    allow_publish = "yes" if allow_publish_input.lower() in {"yes", "y", "да"} else "no"

    # -------------------------------------------------------------------------
    # СОХРАНЕНИЕ ШАГА 1: Обновление site-brief.md
    # -------------------------------------------------------------------------
    print("\n✍️  Сохраняем бриф бизнеса...")
    if brief_path.is_file():
        brief_content = brief_path.read_text(encoding="utf-8")
        
        # Replace placeholders cleanly using regex
        brief_content = re.sub(r"-\s*\*\*site_name:\*\*\s*.*", f"- **site_name:** {site_name}", brief_content)
        brief_content = re.sub(r"-\s*\*\*site_url:\*\*\s*.*", f"- **site_url:** {site_url}", brief_content)
        brief_content = re.sub(r"-\s*\*\*blog_path:\*\*\s*.*", f"- **blog_path:** {blog_path}", brief_content)
        brief_content = re.sub(r"-\s*\*\*niche:\*\*\s*.*", f"- **niche:** {niche}", brief_content)
        brief_content = re.sub(r"-\s*\*\*audience:\*\*\s*.*", f"- **audience:** {audience}", brief_content)
        
        brief_path.write_text(brief_content, encoding="utf-8")
        print(f"✅ Файл '{brief_path.relative_to(root)}' успешно обновлен.")
    else:
        print(f"⚠️  Предупреждение: файл '{brief_path}' не найден. Пропускаем обновление брифа.")

    # -------------------------------------------------------------------------
    # СОХРАНЕНИЕ ШАГА 2: Создание site.env.local
    # -------------------------------------------------------------------------
    print("🔒 Создаем защищенный файл доступов site.env.local...")
    env_content = f"""# Excalibur BLOG — credentials (автоматически сгенерировано setup.py)

PUBLIC_SITE_URL={site_url}
SSH_HOST={ssh_host}
SSH_PORT={ssh_port}
SSH_USER={ssh_user}
SSH_PASS={ssh_pass}
SSH_ROOT={ssh_root}
EXCALIBUR_BLOG_ALLOW_PUBLISH={allow_publish}
"""
    env_path.write_text(env_content, encoding="utf-8")
    print(f"✅ Файл '{env_path.relative_to(root)}' успешно создан.")

    # Создадим пример, если его вдруг нет
    if not env_example_path.is_file():
        example_content = """# Excalibur BLOG — credentials (copy to site.env.local)

PUBLIC_SITE_URL=https://avtosales125.ru
SSH_HOST=djinoum7.beget.tech
SSH_PORT=22
SSH_USER=
SSH_PASS=
SSH_ROOT=/avtosales125/public_html
FTP_HOST=djinoum7.beget.tech
FTP_ROOT=/
EXCALIBUR_BLOG_ALLOW_PUBLISH=no
CATALOG_URL=https://avto-sales125.ru/
TELEGRAM_URL=https://t.me/avtosales125
"""
        env_example_path.write_text(example_content, encoding="utf-8")

    # -------------------------------------------------------------------------
    # ФИНАЛ: Завершение и дальнейшие шаги
    # -------------------------------------------------------------------------
    print("\n" + "="*60)
    print("🎉 Ура! Первоначальная настройка Excalibur BLOG успешно завершена! 🎉")
    print("="*60)
    print("\nЧто делать дальше:")
    print("1. Запустите Scout-агента для поиска новых трендовых тем и наполнения пула:")
    print("   👉 Запустите субагента: Task(excalibur-blog-scout)")
    print("\n2. Либо запустите полный автоматический пайплайн для темы AS01:")
    print("   👉 Выполните в терминале:")
    print("      python scripts/excalibur_blog_today.py")
    print("      python scripts/excalibur_blog_research_start.py --topic-id AS01")
    print("   👉 Затем запустите Директора: excalibur-blog-director")
    print("\nУдачной и легкой автоматизации вашего контента в 2026 году! 🚀\n")

    return 0

if __name__ == "__main__":
    sys.exit(main())
