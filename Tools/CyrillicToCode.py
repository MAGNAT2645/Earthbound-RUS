import sys

table = {
	"А": "[71]",
	"Б": "[72]",
	"В": "[73]",
	"Г": "[74]",
	"Д": "[75]",
	"Е": "[76]",
	"Ё": "[77]",
	"Ж": "[78]",
	"З": "[79]",
	"И": "[7A]",
	"Й": "[7B]",
	"К": "[7C]",
	"Л": "[7D]",
	"М": "[7E]",
	"Н": "[7F]",
	"О": "[80]",
	"П": "[81]",
	"Р": "[82]",
	"С": "[83]",
	"Т": "[84]",
	"У": "[85]",
	"Ф": "[86]",
	"Х": "[87]",
	"Ц": "[88]",
	"Ч": "[89]",
	"Ш": "[8A]",

	"а": "[91]",
	"б": "[92]",
	"в": "[93]",
	"г": "[94]",
	"д": "[95]",
	"е": "[96]",
	"ё": "[97]",
	"ж": "[98]",
	"з": "[99]",
	"и": "[9A]",
	"й": "[9B]",
	"к": "[9C]",
	"л": "[9D]",
	"м": "[9E]",
	"н": "[9F]",
	"о": "[A0]",
	"п": "[A1]",
	"р": "[A2]",
	"с": "[A3]",
	"т": "[A4]",
	"у": "[A5]",
	"ф": "[A6]",
	"х": "[A7]",
	"ц": "[A8]",
	"ч": "[A9]",
	"ш": "[AA]",

	"Щ": "[B0]",
	"Ъ": "[B1]",
	"Ы": "[B2]",
	"Ь": "[B3]",
	"Э": "[B4]",
	"Ю": "[B5]",
	"Я": "[B6]",

	"щ": "[C0]",
	"ъ": "[C1]",
	"ы": "[C2]",
	"ь": "[C3]",
	"э": "[C4]",
	"ю": "[C5]",
	"я": "[C6]"

#	"Y": "[BF]", "r": "[C7]", "t": "[C8]", "h": "[C9]", "u": "[CA]", "n": "[CB]", "d": "[CC]"
}
lookup = {}
for key, value in table.items():
	lookup[value] = key

def convert(char):
	return table.get(char, char)

def deconvert(char):
	return lookup.get(char, char)

getfile = sys.argv[1]
with open(getfile, encoding="utf-8") as fd:
	if len(sys.argv) >= 3 and sys.argv[2] == "1":
		i = 0
		b = []
		a = fd.read()
		while i < len(a):
			if a[i:i + 4] in lookup:
				b.append(lookup[a[i:i + 4]])
				i += 4
			else:
				b.append(a[i])
				i += 1
		converted = "".join(b)
	else:
		converted = "".join(map(convert, fd.read()))

with open("output.txt", mode="w", encoding="utf-8") as fd:
	fd.write(converted)

print('Processed', getfile, 'successfully!')