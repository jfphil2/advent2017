#!/usr/bin/env python3


TEST_INPUT_PART1 = """
5 1 9 5
7 5 3
2 4 6 8
"""

TEST_INPUT_PART2 = """
5 9 2 8
9 4 7 3
3 8 6 5
"""

INPUT = """
414	382	1515	319	83	1327	116	391	101	749	1388	1046	1427	105	1341	1590
960	930	192	147	932	621	1139	198	865	820	597	165	232	417	19	183
3379	987	190	3844	1245	1503	3151	3349	2844	4033	175	3625	3565	179	3938	184
116	51	32	155	102	92	65	42	48	91	74	69	52	89	20	143
221	781	819	121	821	839	95	117	626	127	559	803	779	543	44	369
199	2556	93	1101	122	124	2714	625	2432	1839	2700	2636	118	2306	1616	2799
56	804	52	881	1409	47	246	1368	1371	583	49	1352	976	400	1276	1240
1189	73	148	1089	93	76	3205	3440	3627	92	853	95	3314	3551	2929	3626
702	169	492	167	712	488	357	414	187	278	87	150	19	818	178	686
140	2220	1961	1014	2204	2173	1513	2225	443	123	148	580	833	1473	137	245
662	213	1234	199	1353	1358	1408	235	917	1395	1347	194	565	179	768	650
119	137	1908	1324	1085	661	1557	1661	1828	1865	432	110	658	821	1740	145
1594	222	4140	963	209	2782	180	2591	4390	244	4328	3748	4535	192	157	3817
334	275	395	128	347	118	353	281	430	156	312	386	160	194	63	141
146	1116	153	815	2212	2070	599	3018	2640	47	125	2292	165	2348	2694	184
1704	2194	1753	146	2063	1668	1280	615	163	190	2269	1856	150	158	2250	2459
"""


def corruption_checksum_part1(input):
    checksum = 0
    for line in input.split('\n'):
        if line:
            checksum += row_difference(line)
    return checksum


def row_difference(line):
    min = None
    max = None
    for entry in line.split():
        value = int(entry)
        if not min or value < min:
            min = value
        if not max or value > max:
            max = value
    return max - min


def test_part1(input, expected):
    actual = corruption_checksum_part1(input)
    print('[corruption_checksum_part1({}) = {}] == {}'.format(
            input, actual, expected))
    assert actual == expected


def test_row_differences(input, expected):
    actual = row_difference(input)
    print('[row_difference({}) = {}] == {}'.format(input, actual, expected))
    assert actual == expected


def corruption_checksum_part2(input):
    checksum = 0
    for line in input.split('\n'):
        if line:
            checksum += row_dividend_result(line)
    return checksum


def row_dividend_result(line):
    for divisor in line.split():
        divisor = int(divisor)
        for dividend in line.split():
            dividend = int(dividend)
            if dividend != divisor and dividend % divisor == 0:
                return int(dividend / divisor)


def test_part2(input, expected):
    actual = corruption_checksum_part2(input)
    print('[corruption_checksum_part2({}) = {}] == {}'.format(
            input, actual, expected))
    assert actual == expected


def test_row_dividend_result(input, expected):
    actual = row_dividend_result(input)
    print('[row_dividend_result({}) = {}] == {}'.format(
            input, actual, expected))
    assert actual == expected


if __name__ == '__main__':
    part1_test_data = {"5 1 9 5": 8, "7 5 3": 4, "2 4 6 8": 6}
    for line, expected in part1_test_data.items():
        test_row_differences(line, expected)
    test_part1(TEST_INPUT_PART1, sum(part1_test_data.values()))
    print('Part One Solution:', corruption_checksum_part1(INPUT))

    part2_test_data = {"5 9 2 8": 4, "9 4 7 3": 3, "3 8 6 5": 2}
    for line, expected in part2_test_data.items():
        test_row_dividend_result(line, expected)
    test_part2(TEST_INPUT_PART2, sum(part2_test_data.values()))
    print('Part Two Solution:', corruption_checksum_part2(INPUT))
