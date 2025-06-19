from app import app, db, Verb

def initialize_database():
    """データベースを初期化し、必要に応じて初期データを追加します。"""
    with app.app_context():
        db.create_all()
        if Verb.query.count() == 0:
            initial_verbs = [
                ("cut", "cut", "cut"), ("hit", "hit", "hit"), ("put", "put", "put"), ("set", "set", "set"),
                ("become", "became", "become"), ("come", "came", "come"), ("run", "ran", "run"),
                ("bring", "brought", "brought"), ("build", "built", "built"), ("buy", "bought", "bought"),
                ("catch", "caught", "caught"), ("feel", "felt", "felt"), ("find", "found", "found"),
                ("have", "had", "had"), ("hear", "heard", "heard"), ("keep", "kept", "kept"),
                ("learn", "learned (learnt)", "learned (learnt)"), ("leave", "left", "left"),
                ("lose", "lost", "lost"), ("make", "made", "made"), ("meet", "met", "met"),
                ("pay", "paid", "paid"), ("read", "read", "read"), ("say", "said", "said"),
                ("sell", "sold", "sold"), ("send", "sent", "sent"), ("sit", "sat", "sat"),
                ("sleep", "slept", "slept"), ("spend", "spent", "spent"), ("stand", "stood", "stood"),
                ("teach", "taught", "taught"), ("tell", "told", "told"), ("think", "thought", "thought"),
                ("understand", "understood", "understood"), ("win", "won", "won"),
                ("begin", "began", "begun"), ("break", "broke", "broken"), ("do", "did", "done"),
                ("drink", "drank", "drunk"), ("drive", "drove", "driven"), ("eat", "ate", "eaten"),
                ("get", "got", "got (gotten)"), ("give", "gave", "given"), ("go", "went", "gone"),
                ("know", "knew", "known"), ("rise", "rose", "risen"), ("see", "saw", "seen"),
                ("show", "showed", "shown (showed)"), ("sing", "sang", "sung"),
                ("speak", "spoke", "spoken"), ("swim", "swam", "swum"), ("take", "took", "taken"),
                ("wake", "woke", "woken"), ("wear", "wore", "worn"), ("write", "wrote", "written")
            ]
            verbs_to_add = [Verb(infinitive=inf, past_simple=ps, past_participle=pp) for inf, ps, pp in initial_verbs]
            db.session.bulk_save_objects(verbs_to_add)
            db.session.commit()
            print("データベースに初期データを追加しました。")
        else:
            print("データベースには既にデータが存在します。")

if __name__ == "__main__":
    initialize_database()