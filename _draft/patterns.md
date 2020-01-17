" (212) 123-2345": ^\s*\(\d[3]\)\s*\d[3]-\d[4]\s*$
"intersection": [\w&&[^1-9]]
"union": [a-f0-9]
"alternation": uno|dos|tres
"character set": []
"grouping": ()
"anchoring": ^$
"alternation": |
"(default)greedy": match any much as possible, scan from the last chacter then back off
"? lazy": match as little as possible, scan from the first character till find the match, then no more
"+ posessive": like greedy but no back off
"case insensitive": (?i)
"case match exactly": (?-i)
"back references": \1 or \k<name>
	"replacement": $1 or ${name}