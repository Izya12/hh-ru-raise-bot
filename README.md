# Automatically Raise Your Resume on HH.RU!
A Python Selenium & GitHub Actions bot that automatically raises Your resume in the list on hh.ru

## GitHub Actions github.com/nakigoe/hh-ru-raise-bot/.github/workflows/raise.yml
```
name: Run Python Selenium headless script to raise a resume in the list on hh.ru

# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the "main" branch
  schedule:
    - cron: '0 0 * * *'
    - cron: '5 4 * * *'
    - cron: '10 8 * * *'
    - cron: '15 12 * * *'
    - cron: '20 16 * * *'
    - cron: '25 20 * * *'
    - cron: "0 */4 * * *"

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v3
      
      # Install Python
      - name: setup python
        uses: actions/setup-python@v3
        with:
          python-version: 3.x #install the python needed

      - name: execute py script # run the run.py to get the latest data
        run: |
          pip install --upgrade pip
          pip install selenium
      
      - name: Raise the resume
        run:
          python ./bot/raise.py
        env:
          LOGIN: ${{ secrets.LOGIN }}
          KEY: ${{ secrets.KEY }} 
```

## Usage
1) Clone the repository
2) Create Your own secret keys for GitHub Actions to login into HH.RU: LOGIN and KEY

Everything is mission ready: Your resume will be raised every four hours on hh.ru automatically! 

# HH.RU автоматическое поднятие резюме в списке каждые четыре часа
Бот на Python Selenium и GitHub Actions, автоматически поднимает Ваше резюме в списке на hh.ru

Всё настроено для использования бота на GitHub:
1) клонируйте репозиторий; 
2) создайте Ваши собственные ключи (secrets) уже Вашем репозитории в разделе GitHub Actions: LOGIN и KEY (Ваш логин и пароль к hh.ru) 

<h4 id="github-actions-token">2.5.2 Создание токена удалённого доступа к репозиторию GitHub</h4>
<p>В настройках репозитория на GitHub создайте <em>токен удалённого доступа</em> к репозиторию, комментарий к нему можно выбрать любой, но лучше включить в комментарий название репозитория, так как этих ключей становится несколько, если Вы всерьёз работаете с платформой GitHub.</p>
<p><a class="link" href="https://github.com/settings/tokens" target="_blank">github.com/settings/tokens</a> перейдите по ссылке и выберите в меню
<br> <em>«создать новый токен (классический)»</em>
<br> <em class="ocean-italic">«generate new token (classic)»</em>
<br> и создайте токен с правами доступа <strong>repo</strong> (поставить первую общую галочку, выделяющую первую секцию списка), скриншот&nbsp;1:</p>
<div style="max-width: 1366px; margin: 0 auto;">
<img class="full" src="https://nakigoe.org/_IMG/github-repo-token.png"
  width="1366"
  height="768"
  alt="Создание классического ключа доступа к репозиторию GitHub">
</div>
<p class="wrapper">Скриншот 1 Создание классического ключа доступа к репозиторию GitHub по адресу
<br> <a class="link" href="https://github.com/settings/tokens" target="_blank">github.com/settings/tokens</a></p>

<h4 id="github-actions-access">Внесение токена удалённого доступа в Github&nbsp;Actions</h4>
<p>Чтобы быстро найти страницу создания нового ключа GitHub Actions, Вы можете перейти по сноске:
<br> <em>github.com/ваш&#8209;ник/название&#8209;репозитория/settings/secrets/actions/new</em>
<br> (внесите соответствующие изменения: ваш ник и название репозитория).</p>
<p>В настройках GitHub Actions для репозитория создайте новый <em>секретный&nbsp;ключ,</em> назовите его LOGIN (убедитесь, что название ключа точно такое же, как Вы указали в файле <em>raise.yml</em>):
<br> <code>LOGIN: ${{ secrets.LOGIN }}</code>
<br> и сохраните в секретном ключе GitHub Actions сгенерированный токен удалённого доступа к репозиторию из пункта (1), смотрите ниже скриншот&nbsp;2:</p>
<div style="max-width: 1366px; margin: 0 auto;">
<img class="full" src="https://nakigoe.org/_IMG/github-repo-access.png"
  width="1366"
  height="768"
  alt="Создание классического ключа доступа к репозиторию GitHub">
</div>
 
<p class="wrapper">Скриншот 2 Подключение микро&#8209;сервера GitHub&nbsp;Actions к коду репозитория GitHub при помощи ранее сгенерированного ключа доступа к репозиторию (смотри Скриншот&nbsp;1), ключ доступа для GitHub&nbsp;Actions к репозиторию прописывается по сноске<br> <em>github.com/ваш-ник/название-репозитория/settings/secrets/actions/new</em></p>
<p>Этот ключ (secret) позволяет микро-серверу GitHub Actions считывать код сайта из репозитория GitHub для установки Python, библиотек Selenium, публикации, компрессии и запуска скрипта Python прямо на микросервере GitHub&nbsp;Actions!</p>

Вам необходимо создать ДВА ключа, LOGIN и KEY, содержание — Ваш логин и пароль к hh.ru.
Всё готово: бот запускается автоматически каждые четыре часа.

<br> Пишите, если Вы хотите получить уроки создания вебсайтов: nakigoetenshi@gmail.com
<br> 1000 рублей 2 часа один урок

<h2 style="margin: 0 auto" align="center">Ставьте звёзды и делитесь сноской на репозиторий со всеми, кто искал работу, ищет работу, планирует искать работу!</h2>
<br>
<p style="margin: 0 auto" align="center">Посетите:</p>
<h1><a href="https://nakigoe.org/ru/" style="background-color: black;" target="_blank">
  <img style="display: block; width: calc(100vw - (100vw - 100%));"
    src="https://nakigoe.org/_IMG/logo.png" 
    srcset="https://nakigoe.org/_IMG/logo.png 4800w,
      https://nakigoe.org/_SRC/logo-3840.png 3840w,
      https://nakigoe.org/_SRC/logo-2560.png 2560w,
      https://nakigoe.org/_SRC/logo-2400.png 2400w,
      https://nakigoe.org/_SRC/logo-2048.png 2048w,
      https://nakigoe.org/_SRC/logo-1920.png 1920w,
      https://nakigoe.org/_SRC/logo-1600.png 1600w,
      https://nakigoe.org/_SRC/logo-1440.png 1440w,
      https://nakigoe.org/_SRC/logo-1280.png 1280w,
      https://nakigoe.org/_SRC/logo-1200.png 1200w,
      https://nakigoe.org/_SRC/logo-1080.png 1080w,
      https://nakigoe.org/_SRC/logo-960.png 960w,
      https://nakigoe.org/_SRC/logo-720.png 720w,
      https://nakigoe.org/_SRC/logo-600.png 600w,
      https://nakigoe.org/_SRC/logo-480.png 480w,
      https://nakigoe.org/_SRC/logo-300.png 300w"
    alt="NAKIGOE.ORG">
<img class="blend" style="display: block; width: calc(100vw - (100vw - 100%));" 
  src="https://nakigoe.org/_IMG/nakigoe-academy-night.jpg" 
  srcset="https://nakigoe.org/_IMG/nakigoe-academy-night.jpg 2800w,
    https://nakigoe.org/_SRC/nakigoe-academy-night-2048.jpg 2048w"
  alt="Nakigoe Academy">
  <img class="blend" style="display: block; width: calc(100vw - (100vw - 100%)); padding-bottom: 0.05em;"
    src="https://nakigoe.org/_IMG/logo-hot-bevel.png" 
    srcset="https://nakigoe.org/_IMG/logo-hot-bevel.jpg 4800w,
      https://nakigoe.org/_SRC/logo-hot-bevel-3840.jpg 3840w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2560.jpg 2560w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2400.jpg 2400w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2048.jpg 2048w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1920.jpg 1920w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1600.jpg 1600w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1440.jpg 1440w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1280.jpg 1280w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1200.jpg 1200w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1080.jpg 1080w,
      https://nakigoe.org/_SRC/logo-hot-bevel-960.jpg 960w,
      https://nakigoe.org/_SRC/logo-hot-bevel-720.jpg 720w,
      https://nakigoe.org/_SRC/logo-hot-bevel-600.jpg 600w,
      https://nakigoe.org/_SRC/logo-hot-bevel-480.jpg 480w,
      https://nakigoe.org/_SRC/logo-hot-bevel-300.jpg 300w"
    alt="NAKIGOE.ORG">
</a></h1>
