# Ещё способы запускать скрипт в блендере и редактировать отдельно
# описаны тут - https://docs.blender.org/api/current/info_tips_and_tricks.html#use-an-external-editor

filename = "E:/code/blender_scripts/N_panel_menu/main.py"
exec(compile(open(filename).read(), filename, 'exec'))
