import json
import os

with open('lang.json', mode='rt', encoding='utf-8') as inputfile:
    lang_dict = json.load(inputfile)

for filename in os.listdir('.'):
    if '.lang' in filename:
        print(filename)
        with open(filename, mode='rt', encoding='utf-8') as inputfile:
            content = inputfile.read()
            for lang in lang_dict:
                print('\t', lang)
                lang_content = content
                key_dict = lang_dict[lang]['keys']
                lang_content = lang_content.replace('{%lang%}', lang)
                for key in key_dict:
                    lang_content = lang_content.replace('{%' + key + '%}', key_dict[key])
                suffix = lang_dict[lang]['file_suffix']
                lang_file = filename.replace('.lang', suffix)
                with open(lang_file, mode='wt', encoding='utf-8') as outputfile:
                    outputfile.write(lang_content)
