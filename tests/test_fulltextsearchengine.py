import fulltextsearchengine


class TestEngine:
    def test_save_and_search(self):
        engine = fulltextsearchengine.createSimplestEngine()

        text1 = "ここは東京ですか、東京ではないですか。"
        text2 = "ここは東京です。"
        text3 = "ここは埼玉です。"
        text4 = "ここは東京の東京による東京のための東京です。"

        id1 = engine.save(text1)
        id2 = engine.save(text2)
        engine.save(text3)
        id4 = engine.save(text4)

        actual = engine.search("東京")

        expected = [(id4, text4), (id1, text1), (id2, text2)]

        assert actual == expected
