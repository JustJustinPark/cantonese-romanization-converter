import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import pytest

import cantonese_romanization_converter as crc

class TestJyutpingToYale:
    def test_initials(self):
        encoded = crc.encode("baa3 paa3 maa3 faa3 daa3 taa3 naa3 laa3", crc.System.JYUTPING)
        decoded = crc.decode(encoded, crc.System.YALE)
        assert decoded == "ba pa ma fa da ta na la"
        encoded = crc.encode("gaa3 kaa3 ngaa3 haa3 gwaa3 kwaa3 waa3", crc.System.JYUTPING)
        decoded = crc.decode(encoded, crc.System.YALE)
        assert decoded == "ga ka nga ha gwa kwa wa"
        encoded = crc.encode("zaa3 caa3 saa3 jaa3", crc.System.JYUTPING)
        decoded = crc.decode(encoded, crc.System.YALE)
        assert decoded == "ja cha sa ya"

    def test_finals(self):
        encoded = crc.encode("aa3 aai3 aau3 aam3 aan3 aang3 aap3 aat3 aak3", crc.System.JYUTPING)
        decoded = crc.decode(encoded, crc.System.YALE)
        assert decoded == "a aai aau aam aan aang aap aat aak"
        encoded = crc.encode("a3 ai3 au3 am3 an3 ang3 ap3 at3 ak3", crc.System.JYUTPING)
        decoded = crc.decode(encoded, crc.System.YALE)
        assert decoded == "a ai au am an ang ap at ak"
        encoded = crc.encode("e3 ei3 eu3 em3 eng3 ep3 et3 ek3", crc.System.JYUTPING)
        decoded = crc.decode(encoded, crc.System.YALE)
        assert decoded == "e ei eu em eng ep et ek"
        encoded = crc.encode("i3 iu3 im3 in3 ing3 ip3 it3 ik3", crc.System.JYUTPING)
        decoded = crc.decode(encoded, crc.System.YALE)
        assert decoded == "i iu im in ing ip it ik"
        encoded = crc.encode("o3 oi3 ou3 on3 ong3 ot3 ok3", crc.System.JYUTPING)
        decoded = crc.decode(encoded, crc.System.YALE)
        assert decoded == "o oi ou on ong ot ok"
        encoded = crc.encode("u3 ui3 un3 ung3 ut3 uk3", crc.System.JYUTPING)
        decoded = crc.decode(encoded, crc.System.YALE)
        assert decoded == "u ui un ung ut uk"
        encoded = crc.encode("eoi3 eon3 eot3", crc.System.JYUTPING)
        decoded = crc.decode(encoded, crc.System.YALE)
        assert decoded == "eui eun eut"
        encoded = crc.encode("oe3 oeng3 oet3 oek3", crc.System.JYUTPING)
        decoded = crc.decode(encoded, crc.System.YALE)
        assert decoded == "eu eung eut euk"
        encoded = crc.encode("jyu3 jyun3 jyut3", crc.System.JYUTPING)
        decoded = crc.decode(encoded, crc.System.YALE)
        assert decoded == "yu yun yut"
        encoded = crc.encode("m4 ng5", crc.System.JYUTPING)
        decoded = crc.decode(encoded, crc.System.YALE)
        assert decoded == "mh ńgh"

    def test_tones(self):
        encoded = crc.encode("saam1 gau2 sei3 ling4 ng5 ji6 cat1 baat3 luk6", crc.System.JYUTPING)
        decoded = crc.decode(encoded, crc.System.YALE)
        assert decoded == "sāam gáu sei lìhng ńgh yih chāt baat luhk"

    def test_basic_sentences(self):
        encoded = crc.encode("ngo5 hai6 zung1 gwok3 jan4", crc.System.JYUTPING)
        decoded = crc.decode(encoded, crc.System.YALE)
        assert decoded == "ngóh haih jūng gwok yàhn"

class TestYaleToJyutping:
    def test_initials(self):
        encoded = crc.encode("ba pa ma fa da ta na la", crc.System.YALE)
        decoded = crc.decode(encoded, crc.System.JYUTPING)
        assert decoded == "baa3 paa3 maa3 faa3 daa3 taa3 naa3 laa3"
        encoded = crc.encode("ga ka nga ha gwa kwa wa", crc.System.YALE)
        decoded = crc.decode(encoded, crc.System.JYUTPING)
        assert decoded == "gaa3 kaa3 ngaa3 haa3 gwaa3 kwaa3 waa3"
        encoded = crc.encode("ja cha sa ya", crc.System.YALE)
        decoded = crc.decode(encoded, crc.System.JYUTPING)
        assert decoded == "zaa3 caa3 saa3 jaa3"

    def test_finals(self):
        encoded = crc.encode("a aai aau aam aan aang aap aat aak", crc.System.YALE)
        decoded = crc.decode(encoded, crc.System.JYUTPING)
        assert decoded == "aa3 aai3 aau3 aam3 aan3 aang3 aap3 aat3 aak3"
        encoded = crc.encode("a ai au am an ang ap at ak", crc.System.YALE)
        decoded = crc.decode(encoded, crc.System.JYUTPING)
        assert decoded == "aa3 ai3 au3 am3 an3 ang3 ap3 at3 ak3"
        encoded = crc.encode("e ei eu em eng ep et ek", crc.System.YALE)
        decoded = crc.decode(encoded, crc.System.JYUTPING)
        assert decoded == "e3 ei3 eu3 em3 eng3 ep3 et3 ek3"
        encoded = crc.encode("i iu im in ing ip it ik", crc.System.YALE)
        decoded = crc.decode(encoded, crc.System.JYUTPING)
        assert decoded == "i3 iu3 im3 in3 ing3 ip3 it3 ik3"
        encoded = crc.encode("o oi ou on ong ot ok", crc.System.YALE)
        decoded = crc.decode(encoded, crc.System.JYUTPING)
        assert decoded == "o3 oi3 ou3 on3 ong3 ot3 ok3"
        encoded = crc.encode("u ui un ung ut uk", crc.System.YALE)
        decoded = crc.decode(encoded, crc.System.JYUTPING)
        assert decoded == "u3 ui3 un3 ung3 ut3 uk3"
        encoded = crc.encode("eui eun eut", crc.System.YALE)
        decoded = crc.decode(encoded, crc.System.JYUTPING)
        assert decoded == "eoi3 eon3 eot3"
        encoded = crc.encode("eu eung eut euk", crc.System.YALE)
        decoded = crc.decode(encoded, crc.System.JYUTPING)
        assert decoded == "eu3 oeng3 eot3 oek3"
        encoded = crc.encode("yu yun yut", crc.System.YALE)
        decoded = crc.decode(encoded, crc.System.JYUTPING)
        assert decoded == "jyu3 jyun3 jyut3"
        encoded = crc.encode("mh ńgh", crc.System.YALE)
        decoded = crc.decode(encoded, crc.System.JYUTPING)
        assert decoded == "m4 ng5"

    def test_tones(self):
        encoded = crc.encode("sāam gáu sei lìhng ńgh yih chāt baat luhk", crc.System.YALE)
        decoded = crc.decode(encoded, crc.System.JYUTPING)
        assert decoded == "saam1 gau2 sei3 ling4 ng5 ji6 cat1 baat3 luk6"

    def test_basic_sentences(self):
        encoded = crc.encode("ngóh haih jūng gwok yàhn", crc.System.YALE)
        decoded = crc.decode(encoded, crc.System.JYUTPING)
        assert decoded == "ngo5 hai6 zung1 gwok3 jan4"