import os
import re
from os.path import join

from cold_ray_norilsk.cold_ray_norilsk.src.application.locs import languages

start_reg = "<source>Start</source>\n        <translation type=\"unfinished\"></translation>"
settings_reg = "<source>Settings</source>\n        <translation type=\"unfinished\"></translation>"
suicide_reg = "<source>Suicide</source>\n        <translation type=\"unfinished\"></translation>"
back_reg = "<source>Back</source>\n        <translation type=\"unfinished\"></translation>"


if __name__ == '__main__':
    os.chdir(join("..", "cold_ray_norilsk", "cold_ray_norilsk", "src", "application"))
    for code in languages.codes:
        if code != "en":
            os.system(f"pylupdate5 main_menu.py  -ts " + join("locs", f"en-{code}.ts"))

    for code in languages.codes:
        if code == "en":
            continue
        ts_file = open(join("locs", f"en-{code}.ts"), "r").read()
        ts_file = re.sub(start_reg,
                         f"<source>Start</source>\n        <translation>{languages.ans[code][0]}</translation>",
                         ts_file)
        ts_file = re.sub(settings_reg,
                         f"<source>Settings</source>\n        <translation>{languages.ans[code][1]}</translation>",
                         ts_file)
        ts_file = re.sub(suicide_reg,
                         f"<source>Suicide</source>\n        <translation>{languages.ans[code][2]}</translation>",
                         ts_file)
        ts_file = re.sub(back_reg,
                         f"<source>Back</source>\n        <translation>{languages.ans[code][3]}</translation>",
                         ts_file)
        with open(join("locs", f"en-{code}.ts"), "w", encoding='utf-8') as fout:
            fout.write(ts_file)
        os.system(f"lrelease " + join("locs", f"en-{code}.ts"))
