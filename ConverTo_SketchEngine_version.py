import json

# Sample input data
data = [
{'id': 4, 'text': '( 2 ) Direktiva e Këshillit 91/440/KEE e 29 korrikut 1991 për zhvillimin e hekurudhave të Komunitetit ( 5 ) parashikon disa të drejta përdorimi të transportit hekurudhor ndërkombëtar , për ndërmarrjet hekurudhore dhe grupimet ndërkombëtare të ndërmarrjeve hekurudhore ; këto të drejta nënkuptojnë që infrastruktura hekurudhore mund të përdoret nga shumë përdorues .', 'tokens': [	{'id': 1, 'text': '(', 'upos': 'PUNCT', 'head': 0, 'dspan': (955, 956), 'span': (0, 1), 'lemma': '('},
	{'id': 2, 'text': '2', 'upos': 'NUM', 'feats': 'NumType=Card', 'head': 1, 'dspan': (957, 958), 'span': (2, 3), 'lemma': '2'},
	{'id': 3, 'text': ')', 'upos': 'PUNCT', 'head': 1, 'dspan': (959, 960), 'span': (4, 5), 'lemma': ')'},
	{'id': 4, 'text': 'Direktiva', 'upos': 'NOUN', 'feats': 'Case=Nom|Definite=Def|Gender=Fem|Number=Sing', 'head': 1, 'dspan': (961, 970), 'span': (6, 15), 'lemma': 'direktiva'},
	{'id': 5, 'text': 'e', 'upos': 'DET', 'head': 1, 'dspan': (971, 972), 'span': (16, 17), 'lemma': 'e'},
	{'id': 6, 'text': 'Këshilli', 'upos': 'PROPN', 'feats': 'Case=Nom|Definite=Def|Gender=Masc|Number=Sing', 'head': 1, 'dspan': (973, 981), 'span': (18, 26), 'lemma': 'Këshilli'},
	{'id': 7, 'text': 't', 'upos': 'DET', 'head': 1, 'dspan': (981, 982), 'span': (26, 27), 'lemma': 't'},
	{'id': 8, 'text': '91/440/KEE', 'upos': 'NUM', 'head': 1, 'dspan': (983, 993), 'span': (28, 38), 'lemma': '91/440/kee'},
	{'id': 9, 'text': 'e', 'upos': 'DET', 'head': 1, 'dspan': (994, 995), 'span': (39, 40), 'lemma': 'e'},
	{'id': 10, 'text': '29', 'upos': 'NUM', 'feats': 'NumType=Card', 'head': 1, 'dspan': (996, 998), 'span': (41, 43), 'lemma': '29'},
	{'id': 11, 'text': 'korrikut', 'upos': 'NOUN', 'feats': 'Case=Gen|Definite=Def|Gender=Masc|Number=Sing', 'head': 1, 'dspan': (999, 1007), 'span': (44, 52), 'lemma': 'korrikut'},
	{'id': 12, 'text': '1991', 'upos': 'NUM', 'feats': 'NumType=Card', 'head': 1, 'dspan': (1008, 1012), 'span': (53, 57), 'lemma': '1991'},
	{'id': 13, 'text': 'për', 'upos': 'ADP', 'head': 1, 'dspan': (1013, 1016), 'span': (58, 61), 'lemma': 'për'},
	{'id': 14, 'text': 'zhvillimin', 'upos': 'NOUN', 'feats': 'Case=Acc|Definite=Def|Gender=Masc|Number=Sing', 'head': 1, 'dspan': (1017, 1027), 'span': (62, 72), 'lemma': 'zhvillimin'},
	{'id': 15, 'text': 'e', 'upos': 'DET', 'head': 1, 'dspan': (1028, 1029), 'span': (73, 74), 'lemma': 'e'},
	{'id': 16, 'text': 'hekurudhave', 'upos': 'NOUN', 'feats': 'Case=Acc|Definite=Ind|Gender=Fem|Number=Sing', 'head': 1, 'dspan': (1030, 1041), 'span': (75, 86), 'lemma': 'hekurudhave'},
	{'id': 17, 'text': 'të', 'upos': 'DET', 'head': 1, 'dspan': (1042, 1044), 'span': (87, 89), 'lemma': 'të'},
	{'id': 18, 'text': 'Komunitetit', 'upos': 'NOUN', 'feats': 'Case=Gen|Definite=Def|Gender=Masc|Number=Sing', 'head': 1, 'dspan': (1045, 1056), 'span': (90, 101), 'lemma': 'komunitetit'},
	{'id': 19, 'text': '(', 'upos': 'PUNCT', 'head': 1, 'dspan': (1057, 1058), 'span': (102, 103), 'lemma': '('},
	{'id': 20, 'text': '5', 'upos': 'NUM', 'feats': 'NumType=Card', 'head': 1, 'dspan': (1059, 1060), 'span': (104, 105), 'lemma': '5'},
	{'id': 21, 'text': ')', 'upos': 'PUNCT', 'head': 1, 'dspan': (1061, 1062), 'span': (106, 107), 'lemma': ')'},
	{'id': 22, 'text': 'parashikon', 'upos': 'VERB', 'feats': 'Mood=Ind|Number=Sing|Person=3|Tense=Pres', 'head': 1, 'dspan': (1063, 1073), 'span': (108, 118), 'lemma': 'parashikon'},
	{'id': 23, 'text': 'disa', 'upos': 'PRON', 'feats': 'PronType=Ind', 'head': 1, 'dspan': (1074, 1078), 'span': (119, 123), 'lemma': 'disa'},
	{'id': 24, 'text': 'të drejta', 'upos': 'NOUN', 'head': 1, 'dspan': (1079, 1088), 'span': (124, 133), 'lemma': 'të drejta'},
	{'id': 25, 'text': 'përdorimi', 'upos': 'NOUN', 'feats': 'Case=Nom|Definite=Def|Gender=Masc|Number=Sing', 'head': 1, 'dspan': (1089, 1098), 'span': (134, 143), 'lemma': 'përdorimi'},
	{'id': 26, 'text': 'të', 'upos': 'DET', 'head': 1, 'dspan': (1099, 1101), 'span': (144, 146), 'lemma': 'të'},
	{'id': 27, 'text': 'transportit', 'upos': 'NOUN', 'feats': 'Case=Gen|Definite=Def|Gender=Masc|Number=Sing', 'head': 1, 'dspan': (1102, 1113), 'span': (147, 158), 'lemma': 'transportit'},
	{'id': 28, 'text': 'hekurudhor', 'upos': 'ADJ', 'feats': 'Degre=Pos', 'head': 1, 'dspan': (1114, 1124), 'span': (159, 169), 'lemma': 'hekurudhor'},
	{'id': 29, 'text': 'ndërkombëtar', 'upos': 'ADJ', 'feats': 'Degre=Pos', 'head': 1, 'dspan': (1125, 1137), 'span': (170, 182), 'lemma': 'ndërkombëtar'},
	{'id': 30, 'text': ',', 'upos': 'PUNCT', 'head': 1, 'dspan': (1138, 1139), 'span': (183, 184), 'lemma': ','},
	{'id': 31, 'text': 'për', 'upos': 'ADP', 'head': 1, 'dspan': (1140, 1143), 'span': (185, 188), 'lemma': 'për'},
	{'id': 32, 'text': 'ndërmarrjet', 'upos': 'NOUN', 'feats': 'Case=Acc|Definite=Ind|Gender=Fem|Number=Sing', 'head': 1, 'dspan': (1144, 1155), 'span': (189, 200), 'lemma': 'ndërmarrjet'},
	{'id': 33, 'text': 'hekurudhore', 'upos': 'ADJ', 'feats': 'Degre=Pos', 'head': 1, 'dspan': (1156, 1167), 'span': (201, 212), 'lemma': 'hekurudhore'},
	{'id': 34, 'text': 'dhe', 'upos': 'CCONJ', 'head': 1, 'dspan': (1168, 1171), 'span': (213, 216), 'lemma': 'dhe'},
	{'id': 35, 'text': 'grupimet', 'upos': 'NOUN', 'feats': 'Case=Acc|Definite=Def|Gender=Masc|Number=Plur', 'head': 1, 'dspan': (1172, 1180), 'span': (217, 225), 'lemma': 'grupimet'},
	{'id': 36, 'text': 'ndërkombëtare', 'upos': 'ADJ', 'feats': 'Degre=Pos', 'head': 1, 'dspan': (1181, 1194), 'span': (226, 239), 'lemma': 'ndërkombëtare'},
	{'id': 37, 'text': 'të', 'upos': 'DET', 'head': 1, 'dspan': (1195, 1197), 'span': (240, 242), 'lemma': 'të'},
	{'id': 38, 'text': 'ndërmarrjeve', 'upos': 'NOUN', 'feats': 'Case=Gen|Definite=Def|Gender=Masc|Number=Plur', 'head': 1, 'dspan': (1198, 1210), 'span': (243, 255), 'lemma': 'ndërmarrjeve'},
	{'id': 39, 'text': 'hekurudhore', 'upos': 'ADJ', 'feats': 'Degre=Pos', 'head': 1, 'dspan': (1211, 1222), 'span': (256, 267), 'lemma': 'hekurudhore'},
	{'id': 40, 'text': ';', 'upos': 'PUNCT', 'head': 1, 'dspan': (1223, 1224), 'span': (268, 269), 'lemma': ';'},
	{'id': 41, 'text': 'këto', 'upos': 'PRON', 'feats': 'Case=Acc|Gender=Fem|Number=Plur|PronType=Dem', 'head': 1, 'dspan': (1225, 1229), 'span': (270, 274), 'lemma': 'këto'},
	{'id': 42, 'text': 'të drejta', 'upos': 'NOUN', 'feats': 'Case=Acc|Definite=Ind|Gender=Fem|Number=Plur', 'head': 1, 'dspan': (1230, 1239), 'span': (275, 284), 'lemma': 'të drejta'},
	{'id': 43, 'text': 'nënkuptojnë', 'upos': 'VERB', 'feats': 'Mood=Ind|Number=Plur|Person=3|Tense=Pres', 'head': 1, 'dspan': (1240, 1251), 'span': (285, 296), 'lemma': 'nënkuptojnë'},
	{'id': 44, 'text': 'që', 'upos': 'PRON', 'feats': 'PronType=Rel', 'head': 1, 'dspan': (1252, 1254), 'span': (297, 299), 'lemma': 'që'},
	{'id': 45, 'text': 'infrastruktura', 'upos': 'NOUN', 'feats': 'Case=Nom|Definite=Def|Gender=Fem|Number=Sing', 'head': 1, 'dspan': (1255, 1269), 'span': (300, 314), 'lemma': 'infrastruktura'},
	{'id': 46, 'text': 'hekurudhore', 'upos': 'ADJ', 'feats': 'Degre=Pos', 'head': 1, 'dspan': (1270, 1281), 'span': (315, 326), 'lemma': 'hekurudhore'},
	{'id': 47, 'text': 'mund', 'upos': 'VERB', 'head': 1, 'dspan': (1282, 1286), 'span': (327, 331), 'lemma': 'mund'},
	{'id': 48, 'text': 'të', 'upos': 'DET', 'head': 1, 'dspan': (1287, 1289), 'span': (332, 334), 'lemma': 'të'},
	{'id': 49, 'text': 'përdoret', 'upos': 'VERB', 'feats': 'Mood=Ind|Number=Sing|Person=3|Tense=Pres', 'head': 1, 'dspan': (1290, 1298), 'span': (335, 343), 'lemma': 'përdoret'},
	{'id': 50, 'text': 'nga', 'upos': 'ADP', 'head': 1, 'dspan': (1299, 1302), 'span': (344, 347), 'lemma': 'non'},
	{'id': 51, 'text': 'shumë', 'upos': 'ADV', 'feats': 'AdvType=Deg', 'head': 1, 'dspan': (1303, 1308), 'span': (348, 353), 'lemma': 'shumë'},
	{'id': 52, 'text': 'përdorues', 'upos': 'NOUN', 'feats': 'Case=Acc|Definite=Def|Gender=Masc|Number=Plur', 'head': 1, 'dspan': (1309, 1318), 'span': (354, 363), 'lemma': 'pprdorue'},
	{'id': 53, 'text': '.', 'upos': 'PUNCT', 'head': 1, 'dspan': (1319, 1320), 'span': (364, 365), 'lemma': '.'}], 'dspan': (955, 1320)},
]

current_text_id = None
current_sentence_id = None
vertical_text = ""

# Iterate over each entry in the data
for entry in data:
    text_id = entry['id']  # Each entry has a unique text ID

    # Check if the entry contains tokens
    if 'tokens' in entry:
        tokens = entry['tokens']
        for token in tokens:
            sentence_id = token['head']  # Assuming 'head' indicates the sentence ID

            # Start a new text block if necessary
            if text_id != current_text_id:
                if current_text_id is not None:
                    vertical_text += "</s>\n"
                vertical_text += f"<text id=\"{text_id}\">\n"
                current_text_id = text_id
                current_sentence_id = None

            # Start a new sentence block if necessary
            if sentence_id != current_sentence_id:
                if current_sentence_id is not None:
                    vertical_text += "</s>\n"
                vertical_text += f"<s id=\"{sentence_id}\">\n"
                current_sentence_id = sentence_id

            # Append the word with its POS tag and lemma
            word = token['text']
            lemma = token['lemma']
            pos = token['upos']
            
            vertical_text += f"{word}\t{lemma}\t{pos}\n"

# Close the last sentence and text block
if current_text_id is not None:
    vertical_text += "</s>\n"

output_file_path = "output_vertical_text5.txt"
with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(vertical_text)
