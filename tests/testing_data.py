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
    "url": {
        "ipfs": [
            "http://ipfs.io/ipfs/QmYHNYAaYK5hm3ZhZFx5W9H6xydKDGimjdgJMrMSdnctEm?arg=val#hash",
            "http://ipfs.alexandria.media/ipfs/QmeWz9YZEeNFXQhHg4PnR5ZiNr5isttgi5n1tc1eD5EfGU/content/index.html?arg=val#hash",
            "http://ipfs.io/ipfs/QmYHNYAaYK5hm3ZhZFx5W9H6xydKDGimjdgJMrMSdnctEm",
            "https://gateway.pinata.cloud/ipfs/Qmb4sw3sqA7AZsaRZ7vtMwxCduk1ExJL5gVDPcpnP8kxFK/",
            "https://gateway.pinata.cloud/ipfs/bafybeif5dwlk2sdx5yge4azff2ovsnar63cu37ncw4n24vnqixwamwhxui/",
            "https://bafybeif5dwlk2sdx5yge4azff2ovsnar63cu37ncw4n24vnqixwamwhxui.ipfs.dweb.link/",
        ],
    },
    "subdomain": {
        "ipfs": [
            "http://bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va.ipfs.dweb.link",
            "http://bafybeidvtwx54qr44kidymvhfzefzxhgkieigwth6oswk75zhlzjdmunoy.ipfs.dweb.link/linkify-demo.html",
            "http://bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va.ipfs.localhost:8080",
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
    "url": {
        "ipfs": [
            "http://ipfs.io/ipns/github.com/",
            "https://Qmb4sw3sqA7AZsaRZ7vtMwxCduk1ExJL5gVDPcpnP8kxFK.ipfs.dweb.link/",
            "http://ipfs.io/ipns/QmYHNYAaYK5hm3ZhZFx5W9H6xydKDGimjdgJMrMSdnctEm",
            "https://github.com/ipfs/js-ipfs/blob/master/README.md",
            "https://google.com",
            "http://ipfs.io/ipns/github.com/",
            "https://github.com/ipfs/js-ipfs/blob/master/README.md",
            "http://ipfs.io/ipns/github.com/",
            "https://github.com/ipfs/js-ipfs/blob/master/README.md",
        ],
    },
    "subdomain": {
        "ipfs": [
            "http://bafybeiabc2xofh6tdi6vutusorpumwcikw3hf3st4ecjugo6j52f6xwc6q.ipns.dweb.link",
            "http://not-a-cid.ipfs.dweb.link",
            "http://QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR.ipfs.dweb.link",
            "http://bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va.dweb.link",
            "http://QmcNioXSC1bfJj1dcFErhUfyjFzoX2HodkRccsFFVJJvg8.ipns.dweb.link",
            "http://bafybeiabc2xofh6tdi6vutusorpumwcikw3hf3st4ecjugo6j52f6xwc6q.dweb.link",
            "http://invalid-hostname-.ipns.dweb.link",
            "http://www.bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va.ipfs.dweb.link",
            "http://not-a-cid-or-valid-hostname-.ipns.dweb.link",
        ],
    },
}
