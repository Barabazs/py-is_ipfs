from multibase import encode
import cid

valid_entries = {
    "cid": {
        "v0": [
            "QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",  # base58btc
            "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR",  # base58btc
        ],
        "v1": [
            "0000000010111000000010010001000001100001111000100011100110011111011001000101011111111110100000110110011111001111010011111111101010000111111111100011010111100110100101110110010000101101001100001011100000000000001001011101101110000100101100110100111000011000111011110100101000011100100011010",  # base2
            "72700221014170434637310537764066371723775207774327464566205514134000113556045464703073645034432",  # base8
            "f01701220c3c4733ec8affd06cf9e9ff50ffc6bcd2ec85a6170004bb709669c31de94391a",  # base16
            "bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi",  # base32
            "v05o14863ohpjti5fvk3cv7kvuk7voqud5r45kobg015re2b6jgott51p38",  # base32hex
            "k2jmtxw8rjh1z69c6not3wtdxb0u3urbzhyll1t9jg6ox26dhi5sfi1m",  # base36
            "K2JMTXW8RJH1Z69C6NOT3WTDXB0U3URBZHYLL1T9JG6OX26DHI5SFI1M",  # base36upper
            "ZCJ7vHB6jBiaEvZ1B9N4m6KQ9kWC5bEAXKuzEMRNJzzgHrfXm",  # base58flickr
            "zdj7Wic6KcJAfWz1c9o4M6kq9Lwd5BfbxkVafnrojaaGiSFxM",  # base58btc
            "mAXASIMPEcz7Ir/0Gz56f9Q/8a80uyFphcABLtwlmnDHelDka",  # base64
            "uAXASIMPEcz7Ir_0Gz56f9Q_8a80uyFphcABLtwlmnDHelDka",  # base64url
            "bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va",  # base32
            "zdj7WWeQ43G6JJvLWQWZpyHuAMq6uYWRjkBXFad11vE2LHhQ7",  # base58btc
        ],
        "encoded": [
            cid.from_string("QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"),
            cid.from_string("QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB"),
            cid.from_string(
                "bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va"
            ),
            cid.from_string("zdj7WWeQ43G6JJvLWQWZpyHuAMq6uYWRjkBXFad11vE2LHhQ7"),
            encode("base2", "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"),
            encode("base8", "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"),
            encode("base10", "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"),
            encode("base16", "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"),
            encode("base32", "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"),
            encode("base32hex", "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"),
            encode("base32z", "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"),
            encode("base36", "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"),
            encode("base36upper", "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"),
            encode("base58btc", "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"),
            encode("base58flickr", "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"),
            encode("base64", "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"),
            encode("base64url", "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"),
        ],
    },
    "url": {
        "ipfs": [
            "http://ipfs.io/ipfs/QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR?arg=val#hash",  # base58btc
            "http://ipfs.alexandria.media/ipfs/QmeWz9YZEeNFXQhHg4PnR5ZiNr5isttgi5n1tc1eD5EfGU/content/index.html?arg=val#hash",  # base58btc
            "http://ipfs.io/ipfs/QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR",  # base58btc
            "https://gateway.pinata.cloud/ipfs/Qmb4sw3sqA7AZsaRZ7vtMwxCduk1ExJL5gVDPcpnP8kxFK/",  # base58btc
            "https://gateway.pinata.cloud/ipfs/bafybeif5dwlk2sdx5yge4azff2ovsnar63cu37ncw4n24vnqixwamwhxui/",  # base32
            "https://bafybeif5dwlk2sdx5yge4azff2ovsnar63cu37ncw4n24vnqixwamwhxui.ipfs.dweb.link/",  # base32
            "https://ipfs.io/ipfs/bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi/",  # base32
            "https://ipfs.io/ipfs/f01701220c3c4733ec8affd06cf9e9ff50ffc6bcd2ec85a6170004bb709669c31de94391a",  # base16
            "https://ipfs.io/ipfs/0000000010111000000010010001000001100001111000100011100110011111011001000101011111111110100000110110011111001111010011111111101010000111111111100011010111100110100101110110010000101101001100001011100000000000001001011101101110000100101100110100111000011000111011110100101000011100100011010",  # base2
            "https://ipfs.io/ipfs/ZCJ7vHB6jBiaEvZ1B9N4m6KQ9kWC5bEAXKuzEMRNJzzgHrfXm",  # base58flickr
            "https://ipfs.io/ipfs/zdj7Wic6KcJAfWz1c9o4M6kq9Lwd5BfbxkVafnrojaaGiSFxM",  # base58btc
            "https://ipfs.io/ipfs/QmR7GSQM93Cx5eAg6a6yRzNde1FQv7uL6X1o4k7zrJa3LX/ipfs.draft3.pdf",  # base58btc
        ],
    },
    "subdomain": {
        "ipfs": [
            "http://bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va.ipfs.dweb.link",  # base32
            "http://bafybeidvtwx54qr44kidymvhfzefzxhgkieigwth6oswk75zhlzjdmunoy.ipfs.dweb.link/linkify-demo.html",  # base32
            "http://bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va.ipfs.localhost:8080",  # base32
            "https://bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi.ipfs.dweb.link/",  # base32
            "https://k2jmtxw8rjh1z69c6not3wtdxb0u3urbzhyll1t9jg6ox26dhi5sfi1m.ipfs.dweb.link/",  # base36
        ],
    },
}

invalid_entries = {
    "cid": {
        "all": [
            str("QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR").swapcase(),
            str("QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR").lower(),
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
            "http://ipfs.io/ipns/QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR",
            "https://github.com/ipfs/js-ipfs/blob/master/README.md",
            "https://google.com",
        ],
    },
    "subdomain": {
        "ipfs": [
            "http://bafybeiabc2xofh6tdi6vutusorpumwcikw3hf3st4ecjugo6j52f6xwc6q.ipns.dweb.link",
            "http://not-a-cid.ipfs.dweb.link",
            "http://QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR.ipfs.dweb.link",  # base58btc
            "http://bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va.dweb.link",
            "http://QmcNioXSC1bfJj1dcFErhUfyjFzoX2HodkRccsFFVJJvg8.ipns.dweb.link",  # base58btc
            "http://bafybeiabc2xofh6tdi6vutusorpumwcikw3hf3st4ecjugo6j52f6xwc6q.dweb.link",
            "http://invalid-hostname-.ipns.dweb.link",
            "http://www.bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va.ipfs.dweb.link",
            "http://not-a-cid-or-valid-hostname-.ipns.dweb.link",
            "https://zdj7Wic6KcJAfWz1c9o4M6kq9Lwd5BfbxkVafnrojaaGiSFxM.ipfs.dweb.link",  # base58btc
            "https://f01701220c3c4733ec8affd06cf9e9ff50ffc6bcd2ec85a6170004bb709669c31de94391a.ipfs.dweb.link/",  # base16
            "https://ipfs.io/ipfs/7002700221014170434637310537764066371723775207774327464566205514134000113556045464703073645034432",  # base8
            "https://ipfs.io/ipfs/92793123896416649578508430956173875066425468388805468715479907750778834469731416946970",  # base10
        ],
    },
}
