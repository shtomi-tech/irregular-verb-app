# init_db.py

# 必要な部品をapp.pyからインポート
from app import app, db, Verb

print("データベースのセットアップを開始します...")

# アプリケーションのコンテキスト内でデータベース操作を実行
with app.app_context():
    # 古いテーブルを一度全て削除
    db.drop_all()
    # 新しいテーブルを設計図通りに作成
    db.create_all()

    print("初期データを投入します...")

    # 単語リスト
    initial_verbs = [
        ["cut", "cut", "cut"], ["hit", "hit", "hit"], ["put", "put", "put"], ["set", "set", "set"],
        ["become", "became", "become"], ["come", "came", "come"], ["run", "ran", "run"],
        ["bring", "brought", "brought"], ["build", "built", "built"], ["buy", "bought", "bought"],
        ["catch", "caught", "caught"], ["feel", "felt", "felt"], ["find", "found", "found"],
        ["have", "had", "had"], ["hear", "heard", "heard"], ["keep", "kept", "kept"],
        ["learn", "learned (learnt)", "learned (learnt)"], ["leave", "left", "left"],
        ["lose", "lost", "lost"], ["make", "made", "made"], ["meet", "met", "met"],
        ["pay", "paid", "paid"], ["read", "read", "read"], ["say", "said", "said"],
        ["sell", "sold", "sold"], ["send", "sent", "sent"], ["sit", "sat", "sat"],
        ["sleep", "slept", "slept"], ["spend", "spent", "spent"], ["stand", "stood", "stood"],
        ["teach", "taught", "taught"], ["tell", "told", "told"], ["think", "thought", "thought"],
        ["understand", "understood", "understood"], ["win", "won", "won"],
        ["begin", "began", "begun"], ["break", "broke", "broken"], ["do", "did", "done"],
        ["drink", "drank", "drunk"], ["drive", "drove", "driven"], ["eat", "ate", "eaten"],
        ["get", "got", "got (gotten)"], ["give", "gave", "given"], ["go", "went", "gone"],
        ["know", "knew", "known"], ["rise", "rose", "risen"], ["see", "saw", "seen"],
        ["show", "showed", "shown (showed)"], ["sing", "sang", "sung"],
        ["speak", "spoke", "spoken"], ["swim", "swam", "swum"], ["take", "took", "taken"],
        ["wake", "woke", "woken"], ["wear", "wore", "worn"], ["write", "wrote", "written"]
    ]

    # リストの単語を一つずつデータベースに追加
    for v in initial_verbs:
        db.session.add(Verb(infinitive=v[0], past_simple=v[1], past_participle=v[2]))

    db.session.commit()
    print("データベースに初期データを追加しました。")

print("データベースのセットアップが完了しました。")
