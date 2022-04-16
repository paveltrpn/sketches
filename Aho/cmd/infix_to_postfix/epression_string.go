package main

type expressionString_s struct {
	pos int
	str string
}

func buildExpressionString(str string) expressionString_s {
	return expressionString_s{0, str}
}

func (es *expressionString_s) appenTermToExprStr(term int) {
	es.str = es.str + string(rune(term))
}

func (es *expressionString_s) getNextChar() (int, int) {
	if es.pos+1 > len([]rune(es.str)) {
		return -1, int(' ')
	}

	rt := es.str[es.pos]
	es.pos = es.pos + 1
	return es.pos, int(rt)
}

func (es *expressionString_s) loadNewString(new string) {
	es.str = new
	es.pos = 0
}
