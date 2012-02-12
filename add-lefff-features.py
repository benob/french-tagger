import sys

if len(sys.argv) != 2:
    print >>sys.stderr, "usage: %s <lefff-word-tags>" % sys.argv[0]
    sys.exit(1)

lefff = {}
for line in open(sys.argv[1]):
    tokens = line.strip().split()
    lefff[tokens[0]] = "\t".join(["lefff=" + x for x in tokens[1:]])

for line in sys.stdin:
    tokens = line.strip().split("\t")
    for token in tokens:
        if token.startswith("w[0]="):
            word = token[5:]
            if word in lefff:
                tokens.append(lefff[word])
            break
    print "\t".join(tokens)

