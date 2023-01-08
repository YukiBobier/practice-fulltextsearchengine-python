import fulltextsearchengine


class TestEngine:
    def test_save_and_search(self):
        engine = fulltextsearchengine.createSimplestEngine()

        text1 = "走って走っていやいややっぱ歩いて"
        text2 = "走る雲の影を飛び越えるわ"
        text3 = "上を向いて歩う涙がこぼれないように"
        text4 = "動き出すよ君の元へ走れ！走れ！走れ！"

        id1 = engine.save(text1)
        id2 = engine.save(text2)
        engine.save(text3)
        id4 = engine.save(text4)

        actual = engine.search("走る")

        expected = [(id4, text4), (id1, text1), (id2, text2)]

        assert actual == expected
