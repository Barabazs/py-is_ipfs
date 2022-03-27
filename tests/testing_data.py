from multibase import encode
import cid

valid_entries = {
    "cid": {
        "v0": [
            "QmYjtig7VJQ6XsnUjqqJvj7QaMcCAwtrgNdahSiFofrE7o",
            "QmYHNYAaYK5hm3ZhZFx5W9H6xydKDGimjdgJMrMSdnctEm",
            "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR",
        ],
        "v1": [
            "bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va",
            "bafybeie2reiz2q6rbcuwpy2etyztjnceolu4rdi7rp3th2lsky4r5ckeey",
        ],
        "encoded": [
            cid.from_string("QmYjtig7VJQ6XsnUjqqJvj7QaMcCAwtrgNdahSiFofrE7o"),
            cid.from_string("QmYHNYAaYK5hm3ZhZFx5W9H6xydKDGimjdgJMrMSdnctEm"),
            cid.from_string(
                "bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va"
            ),
            cid.from_string(
                "bafybeie2reiz2q6rbcuwpy2etyztjnceolu4rdi7rp3th2lsky4r5ckeey"
            ),
            cid.from_string("zdj7WWeQ43G6JJvLWQWZpyHuAMq6uYWRjkBXFad11vE2LHhQ7"),
            "zdj7WWeQ43G6JJvLWQWZpyHuAMq6uYWRjkBXFad11vE2LHhQ7",
            encode("base58btc", "QmYjtig7VJQ6XsnUjqqJvj7QaMcCAwtrgNdahSiFofrE7o"),
            encode("base58btc", "QmYHNYAaYK5hm3ZhZFx5W9H6xydKDGimjdgJMrMSdnctEm"),
            encode("base58btc", "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"),
            encode("base58btc", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base2", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base58flickr", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base2", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base8", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base10", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base16", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base16", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base16", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base32hex", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base32", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base32z", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base36", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base36upper", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base58flickr", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base58btc", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base64", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            encode("base64url", "QmNQuBJ8tg4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
            "f01701220c3c4733ec8affd06cf9e9ff50ffc6bcd2ec85a6170004bb709669c31de94391a",
        ],
    },
}
invalid_entries = {
    "cid": {
        "all": [
            str("QmYjtig7VJQ6XsnUjqqJvj7QaMcCAwtrgNdahSiFofrE7o").swapcase(),
            str("QmYjtig7VJQ6XsnUjqqJvj7QaMcCAwtrgNdahSiFofrE7o").lower(),
            "afybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va"
            "bafybeie2reiz2q6rbcuwpy2etyztjnceolu4rdi7rp3th2lsky4r5ckee"
            "QmYjtig7VJQ6XsnUjqqJvj7QaMcCAwtrgNdahSiFofrE70",
            "",
            1234,
            "noop",
            b"QmYjtig7VJQ6XsnUjqqJvj7QaMcCAwtrgNdahSiFofrE70",
            "dfmqjdmfkjqdm",
            "bafybeierhgbz4zp2x2u67urqrgfnrnlukciupzenpqpipiz5nwtq",
            "1234",
            encode("base58btc", "QmYjtig7VJQ6XsnUjqqJvj7QaMcCAwtrgNdahSiFofrE70"),
            encode("base16", "QmNQuBJ8g4QN6mSLXHekxBbcToPwKxamWNrDdEugxMTDd"),
        ]
    },
}
