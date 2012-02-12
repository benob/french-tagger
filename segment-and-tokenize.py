import sys, re

def tokenize(line):
    line = line.decode("utf8")
    line = " " + line + " "
    line = re.sub("[«»]", r'"', line)
    line = re.sub("’", r"'", line)
    line = re.sub("–", r"--", line)
    #line = line.replace("…", "...")
    line = re.sub(r"'(\S)", r"' \1", line)
    line = re.sub(r"([^0-9])([.,])([^0-9])", r"\1 \2 \3", line)
    line = re.sub(r"([;:!?\"\(\)\[\]\{\}/\\<>])", r" \1 ", line)
    line = re.sub(r"-", r" - ", line)
    line = re.sub(r"- ((elle|il)s?|ci|là|moi|nous|vous|y|ce|c'|en|je|on|tu) ", r"-\1 ", line)
    line = re.sub(r"- t -", r"-t-", line)
    line = re.sub(r"- -", r"--", line)
    line = re.sub("(" + "|".join(abbrev) + ") \. ", r"\1.", line)
    line = re.sub(r"(aujourd') (hui)", r"\1\2", line, re.I)
    line = re.sub(r"  +", r" ", line)
    return line.strip().split()

abbrev = set(['adj', 'adv', 'env', 'boul', 'p', 'M', 'MM', 'n', 'N.B', 'O', 'qqf', 'qqch', 'c.-à-d', 'P.-S', 'cell', 'app', 'Pr', 'etc', 'av', 'apr', 'admin', 'Admin', 'ref', 'cf'])

kept = []
for line in sys.stdin:
    line = line.strip()
    while len(line) > 0:
        found = re.match(r"(.*?(\S*[^\sA-ZÉÈËÊÏÎÌÇÛÜÙÀ])[.?!]) ([A-ZÉÈËÊÏÎÌÇÛÜÙÀ])", line)
        if not found:
            kept.append(line)
            for word in tokenize(" ".join(kept)):
                print word
            print
            break
        if found.group(2) not in abbrev:
            kept.append(found.group(1))
            for word in tokenize(" ".join(kept)):
                print word
            print
            kept = []
        else:
            kept.append(found.group(1))
        line = line[len(found.group(1)) + 1:]

