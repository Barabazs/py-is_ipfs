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
            "92793123896416649578508430956173875066425468388805468715479907750778834469731416946970",  # base10
            "f01701220c3c4733ec8affd06cf9e9ff50ffc6bcd2ec85a6170004bb709669c31de94391a",  # base16
            "bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va",  # base32
            "bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi",  # base32
            "v05o14863ohpjti5fvk3cv7kvuk7voqud5r45kobg015re2b6jgott51p38",  # base32hex
            "k2jmtxw8rjh1z69c6not3wtdxb0u3urbzhyll1t9jg6ox26dhi5sfi1m",  # base36
            "K2JMTXW8RJH1Z69C6NOT3WTDXB0U3URBZHYLL1T9JG6OX26DHI5SFI1M",  # base36upper
            "ZCJ7vHB6jBiaEvZ1B9N4m6KQ9kWC5bEAXKuzEMRNJzzgHrfXm",  # base58flickr
            "zdj7Wic6KcJAfWz1c9o4M6kq9Lwd5BfbxkVafnrojaaGiSFxM",  # base58btc
            "zdj7WWeQ43G6JJvLWQWZpyHuAMq6uYWRjkBXFad11vE2LHhQ7",  # base58btc
            "mAXASIMPEcz7Ir/0Gz56f9Q/8a80uyFphcABLtwlmnDHelDka",  # base64
            "uAXASIMPEcz7Ir_0Gz56f9Q_8a80uyFphcABLtwlmnDHelDka",  # base64url
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
            "https://ipfs.io/ipfs/0000000010111000000010010001000001100001111000100011100110011111011001000101011111111110100000110110011111001111010011111111101010000111111111100011010111100110100101110110010000101101001100001011100000000000001001011101101110000100101100110100111000011000111011110100101000011100100011010",  # base2
            "https://ipfs.io/ipfs/f01701220c3c4733ec8affd06cf9e9ff50ffc6bcd2ec85a6170004bb709669c31de94391a",  # base16
            "https://gateway.pinata.cloud/ipfs/bafybeif5dwlk2sdx5yge4azff2ovsnar63cu37ncw4n24vnqixwamwhxui/",  # base32
            "https://ipfs.io/ipfs/bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi/",  # base32
            "https://ipfs.io/ipfs/v05o14863ohpjti5fvk3cv7kvuk7voqud5r45kobg015re2b6jgott51p38",  # base32hex
            "https://ipfs.io/ipfs/k2jmtxw8rjh1z69c6not3wtdxb0u3urbzhyll1t9jg6ox26dhi5sfi1m",  # base36
            "https://ipfs.io/ipfs/K2JMTXW8RJH1Z69C6NOT3WTDXB0U3URBZHYLL1T9JG6OX26DHI5SFI1M",  # base36upper
            "https://ipfs.io/ipfs/ZCJ7vHB6jBiaEvZ1B9N4m6KQ9kWC5bEAXKuzEMRNJzzgHrfXm",  # base58flickr
            "http://ipfs.io/ipfs/QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR?arg=val#hash",  # base58btc
            "http://ipfs.alexandria.media/ipfs/QmeWz9YZEeNFXQhHg4PnR5ZiNr5isttgi5n1tc1eD5EfGU/content/index.html?arg=val#hash",  # base58btc
            "http://ipfs.io/ipfs/QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR",  # base58btc
            "https://gateway.pinata.cloud/ipfs/Qmb4sw3sqA7AZsaRZ7vtMwxCduk1ExJL5gVDPcpnP8kxFK/",  # base58btc
            "https://ipfs.io/ipfs/zdj7Wic6KcJAfWz1c9o4M6kq9Lwd5BfbxkVafnrojaaGiSFxM",  # base58btc
            "https://ipfs.io/ipfs/QmR7GSQM93Cx5eAg6a6yRzNde1FQv7uL6X1o4k7zrJa3LX/ipfs.draft3.pdf",  # base58btc
            "https://ipfs.io/ipfs/uAXASIMPEcz7Ir_0Gz56f9Q_8a80uyFphcABLtwlmnDHelDka",  # base64url
        ],
        "ipns": [
            "http://ipfs.io/ipns/foo.bar/",  # theoretically valid, but is missing a dnslink record
            "https://ipfs.io/ipns/en.wikipedia-on-ipfs.org/wiki/",
            "https://ipfs.io/ipns/01011100100000000000100100000010000000000100010010001000000001101100000000001011010111001111011100001111011011011110000110010010011110000111100011011100010111111100111101110101100110111011011101000001100110101011111110001011000001111110000110000111010100101100011010011000111000101000010101010110100001001100110011",  # base2
            "https://ipfs.io/ipns/f01720024080112201b002d73dc3db78649e1e3717f3dd66edd066afe2c1f861d4b1a638a155a1333",  # base16
            "https://ipfs.io/ipns/bafzaajaiaejcagyafvz5ypnxqze6dy3rp465m3w5azvp4la7qyouwgtdrikvuezt",  # base32
            "https://ipfs.io/ipns/v05p00908049206o05lptofdngp4u3orhfsutcrmt0plfsb0vgoekm6j3h8alk4pj",  # base32hex
            "https://ipfs.io/ipns/k51qzi5uqu5dgutdk6i1ynyzgkqngpha5xpgia3a5qqp4jsh0u4csozksxel2r",  # base36
            "https://ipfs.io/ipns/K51QZI5UQU5DGUTDK6I1YNYZGKQNGPHA5XPGIA3A5QQP4JSH0U4CSOZKSXEL2R",  # base36upper
            "https://ipfs.io/ipns/Z5azMnuicXMgDMqbtbwJiQHydfF5kzhqYommSLcxq57AXAbA8SFnxoB",  # base58flickr CIDv1
            "https://ipfs.io/ipns/z5AanNVJCxnGenRBUBXjJqiZDFg5LaHRyPMMsmCYR57bxbBb8sgNYPc",  # base58btc CIDv1
            "https://ipfs.io/ipns/uAXIAJAgBEiAbAC1z3D23hknh43F_PdZu3QZq_iwfhh1LGmOKFVoTMw",  # base64url
        ],
    },
    "subdomain": {
        "ipfs": [
            "https://bafybeif5dwlk2sdx5yge4azff2ovsnar63cu37ncw4n24vnqixwamwhxui.ipfs.dweb.link/",  # base32
            "http://bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va.ipfs.dweb.link",  # base32
            "http://bafybeidvtwx54qr44kidymvhfzefzxhgkieigwth6oswk75zhlzjdmunoy.ipfs.dweb.link/linkify-demo.html",  # base32
            "http://bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va.ipfs.localhost:8080",  # base32
            "https://bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi.ipfs.dweb.link/",  # base32
            "https://v05o14863ohpjti5fvk3cv7kvuk7voqud5r45kobg015re2b6jgott51p38.ipfs.dweb.link/",  # base32hex
            "https://k2jmtxw8rjh1z69c6not3wtdxb0u3urbzhyll1t9jg6ox26dhi5sfi1m.ipfs.dweb.link/",  # base36
            "https://K2JMTXW8RJH1Z69C6NOT3WTDXB0U3URBZHYLL1T9JG6OX26DHI5SFI1M.ipfs.dweb.link/",  # base36upper
        ],
        "ipns": [
            "http://docs.ipfs.io.ipns.localhost:8080/some/path",
            "http://docs.ipfs.io.ipns.foo.bar.buzz.dweb.link",
            "http://docs.ipfs.io.ipns.locahost:8080",
            "https://en-wikipedia--on--ipfs-org.ipns.dweb.link",
            "https://ipfs-io.ipns.dweb.link/",
            "https://k51qzi5uqu5dgutdk6i1ynyzgkqngpha5xpgia3a5qqp4jsh0u4csozksxel2r.ipns.dweb.link/",  # base36
            "https://K51QZI5UQU5DGUTDK6I1YNYZGKQNGPHA5XPGIA3A5QQP4JSH0U4CSOZKSXEL2R.ipns.dweb.link",  # base36upper
        ],
    },
    "path": {
        "ipfs": [
            "/ipfs/0000000010111000000010010001000001100001111000100011100110011111011001000101011111111110100000110110011111001111010011111111101010000111111111100011010111100110100101110110010000101101001100001011100000000000001001011101101110000100101100110100111000011000111011110100101000011100100011010",  # base2
            "/ipfs/f01701220c3c4733ec8affd06cf9e9ff50ffc6bcd2ec85a6170004bb709669c31de94391a",  # base16
            "/ipfs/bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va",  # base32
            "/ipfs/bafzaajaiaejcbl6sqhrt4bii7kvqtk3ye3jmqllbxxeurgms6iuh52vad7vcc4gy",  # base32
            "/ipfs/v05o14863ohpjti5fvk3cv7kvuk7voqud5r45kobg015re2b6jgott51p38",  # base32hex
            "/ipfs/k51qzi5uqu5dkkciu33khkzbcmxtyhn376i1e83tya8kuy7z9euedzyr5nhoew",  # base36
            "/ipfs/K2JMTXW8RJH1Z69C6NOT3WTDXB0U3URBZHYLL1T9JG6OX26DHI5SFI1M",  # base36upper
            "/ipfs/QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR?arg=val#hash",  # base58btc CIDv0
            "/ipfs/QmeWz9YZEeNFXQhHg4PnR5ZiNr5isttgi5n1tc1eD5EfGU/content/index.html?arg=val#hash",  # base58btc CIDv0
            "/ipfs/ZCJ7vHB6jBiaEvZ1B9N4m6KQ9kWC5bEAXKuzEMRNJzzgHrfXm",  # base58flickr"
            "/ipfs/zdj7Wic6KcJAfWz1c9o4M6kq9Lwd5BfbxkVafnrojaaGiSFxM",  # base58btc CIDv1
            "/ipfs/QmR7GSQM93Cx5eAg6a6yRzNde1FQv7uL6X1o4k7zrJa3LX/ipfs.draft3.pdf",  # base58btc CIDv0
            "/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Aardvark.html",  # base58btc CIDv0
            "/ipfs/uAXASIMPEcz7Ir_0Gz56f9Q_8a80uyFphcABLtwlmnDHelDka",  # base64url
        ],
        "ipns": [
            "/ipns/en-wikipedia--on--ipfs-org.ipns.dweb.link",  # theoretically valid, but is missing a dnslink record
            "/ipns/ipfs-io.ipns.ipfs.io",  # theoretically valid, but is missing a dnslink record
            "/ipns/github.com/",  # theoretically valid, but is missing a dnslink record
            "/ipns/cid.ipfs.io",
            "/ipns/ipfs.io",
            "/ipns/libp2p.io",
            "/ipns/docs.ipfs.io/introduction/",
            "/ipns/en.wikipedia-on-ipfs.org/",
            "/ipns/foo.bar",  # theoretically valid, but is missing a dnslink record
            "/ipns/01011100100000000000100100000010000000000100010010001000000001101100000000001011010111001111011100001111011011011110000110010010011110000111100011011100010111111100111101110101100110111011011101000001100110101011111110001011000001111110000110000111010100101100011010011000111000101000010101010110100001001100110011",  # base2
            "/ipns/f01720024080112201b002d73dc3db78649e1e3717f3dd66edd066afe2c1f861d4b1a638a155a1333",  # base16
            "/ipns/bafzaajaiaejcagyafvz5ypnxqze6dy3rp465m3w5azvp4la7qyouwgtdrikvuezt",  # base32
            "/ipns/v05p00908049206o05lptofdngp4u3orhfsutcrmt0plfsb0vgoekm6j3h8alk4pj",  # base32hex
            "/ipns/k51qzi5uqu5dgutdk6i1ynyzgkqngpha5xpgia3a5qqp4jsh0u4csozksxel2r",  # base36
            "/ipns/K51QZI5UQU5DGUTDK6I1YNYZGKQNGPHA5XPGIA3A5QQP4JSH0U4CSOZKSXEL2R",  # base36upper
            "/ipns/Z5azMnuicXMgDMqbtbwJiQHydfF5kzhqYommSLcxq57AXAbA8SFnxoB",  # base58flickr CIDv1
            "/ipns/z5AanNVJCxnGenRBUBXjJqiZDFg5LaHRyPMMsmCYR57bxbBb8sgNYPc",  # base58btc CIDv1
            "/ipns/uAXIAJAgBEiAbAC1z3D23hknh43F_PdZu3QZq_iwfhh1LGmOKFVoTMw",  # base64url
        ],
    },
    "native_url": {
        "ipfs": [
            "ipfs://QmeWz9YZEeNFXQhHg4PnR5ZiNr5isttgi5n1tc1eD5EfGU",  # CIDv0  base58btc
            "ipfs://bafybeidvtwx54qr44kidymvhfzefzxhgkieigwth6oswk75zhlzjdmunoy/linkify-demo.html",  # base32
            "ipfs://bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi/",  # base32
            "ipfs://k2jmtxw8rjh1z69c6not3wtdxb0u3urbzhyll1t9jg6ox26dhi5sfi1m/",  # base36
            "ipfs://0000000010111000000010010001000001100001111000100011100110011111011001000101011111111110100000110110011111001111010011111111101010000111111111100011010111100110100101110110010000101101001100001011100000000000001001011101101110000100101100110100111000011000111011110100101000011100100011010",  # base2
            "ipfs://f01701220c3c4733ec8affd06cf9e9ff50ffc6bcd2ec85a6170004bb709669c31de94391a",  # base16
            "ipfs://bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va",  # base32
            "ipfs://bafzaajaiaejcbl6sqhrt4bii7kvqtk3ye3jmqllbxxeurgms6iuh52vad7vcc4gy",  # base32
            "ipfs://v05o14863ohpjti5fvk3cv7kvuk7voqud5r45kobg015re2b6jgott51p38",  # base32hex
            "ipfs://k51qzi5uqu5dkkciu33khkzbcmxtyhn376i1e83tya8kuy7z9euedzyr5nhoew",  # base36
            "ipfs://K2JMTXW8RJH1Z69C6NOT3WTDXB0U3URBZHYLL1T9JG6OX26DHI5SFI1M",  # base36upper
            "ipfs://QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR?arg=val#hash",  # base58btc
            "ipfs://QmeWz9YZEeNFXQhHg4PnR5ZiNr5isttgi5n1tc1eD5EfGU/content/index.html?arg=val#hash",  # base58btc CIDv0
            "ipfs://ZCJ7vHB6jBiaEvZ1B9N4m6KQ9kWC5bEAXKuzEMRNJzzgHrfXm",  # base58flickr"
            "ipfs://zdj7Wic6KcJAfWz1c9o4M6kq9Lwd5BfbxkVafnrojaaGiSFxM",  # base58btc CIDv1
            "ipfs://QmR7GSQM93Cx5eAg6a6yRzNde1FQv7uL6X1o4k7zrJa3LX/ipfs.draft3.pdf",  # base58btc
            "ipfs://QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Aardvark.html",  # base58btc
            "ipfs://uAXASIMPEcz7Ir_0Gz56f9Q_8a80uyFphcABLtwlmnDHelDka",  # base64url
        ],
        "ipns": [
            "ipns://en-wikipedia--on--ipfs-org.ipns.dweb.link",  # theoretically valid, but is missing a dnslink record
            "ipns://cid.ipfs.io",
            "ipns://ipfs-io.ipns.ipfs.io",  # theoretically valid, but is missing a dnslink record
            "ipns://ipfs.io",
            "ipns://k51qzi5uqu5dgutdk6i1ynyzgkqngpha5xpgia3a5qqp4jsh0u4csozksxel2r",  # base36
            "ipns://K51QZI5UQU5DGUTDK6I1YNYZGKQNGPHA5XPGIA3A5QQP4JSH0U4CSOZKSXEL2R/path#title",  # base36upper
            "ipns://github.com/",  # theoretically valid, but is missing a dnslink record
            "ipns://libp2p.io",
            "ipns://docs.ipfs.io/introduction/",
            "ipns://en.wikipedia-on-ipfs.org/",
            "ipns://foo.bar",  # theoretically valid, but is missing a dnslink record
            "ipns://01011100100000000000100100000010000000000100010010001000000001101100000000001011010111001111011100001111011011011110000110010010011110000111100011011100010111111100111101110101100110111011011101000001100110101011111110001011000001111110000110000111010100101100011010011000111000101000010101010110100001001100110011",  # base2
            "ipns://f01720024080112201b002d73dc3db78649e1e3717f3dd66edd066afe2c1f861d4b1a638a155a1333",  # base16
            "ipns://bafzaajaiaejcagyafvz5ypnxqze6dy3rp465m3w5azvp4la7qyouwgtdrikvuezt",  # base32
            "ipns://v05p00908049206o05lptofdngp4u3orhfsutcrmt0plfsb0vgoekm6j3h8alk4pj",  # base32hex
            "ipns://k51qzi5uqu5dgutdk6i1ynyzgkqngpha5xpgia3a5qqp4jsh0u4csozksxel2r",  # base36
            "ipns://K51QZI5UQU5DGUTDK6I1YNYZGKQNGPHA5XPGIA3A5QQP4JSH0U4CSOZKSXEL2R",  # base36upper
            "ipns://Z5azMnuicXMgDMqbtbwJiQHydfF5kzhqYommSLcxq57AXAbA8SFnxoB",  # base58flickr CIDv1
            "ipns://z5AanNVJCxnGenRBUBXjJqiZDFg5LaHRyPMMsmCYR57bxbBb8sgNYPc",  # base58btc CIDv1
            "ipns://uAXIAJAgBEiAbAC1z3D23hknh43F_PdZu3QZq_iwfhh1LGmOKFVoTMw",  # base64url
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
            "https://ipfs.io/ipfs/72700221014170434637310537764066371723775207774327464566205514134000113556045464703073645034432",  # base8
            "https://ipfs.io/ipfs/92793123896416649578508430956173875066425468388805468715479907750778834469731416946970",  # base10
            "https://ipfs.io/ipfs/mAXASIMPEcz7Ir/0Gz56f9Q/8a80uyFphcABLtwlmnDHelDka",  # base64
            "https://github.com/ipfs/js-ipfs/blob/master/README.md",
            "https://google.com",
        ],
        "ipns": [
            "https://ipfs.io/ipns/7134400044020004221001540013271734173336062236074334277475654673350146537613017606072454323070502526411463",  # base8
            "https://ipfs.io/ipns/912059270899086145358701227151751949578967872728194642447008830239276889128468550643329311314739",  # base10
            "https://ipfs.io/ipns/mAXIAJAgBEiAbAC1z3D23hknh43F/PdZu3QZq/iwfhh1LGmOKFVoTMw",  # base64
            "https://github.com/ipns/js-ipfs/blob/master/README.md",
            "https://google.com",
        ],
    },
    "subdomain": {
        "ipfs": [
            "https://010111000000010010001000001100001111000100011100110011111011001000101011111111110100000110110011111001111010011111111101010000111111111100011010111100110100101110110010000101101001100001011100000000000001001011101101110000100101100110100111000011000111011110100101000011100100011010.ipfs.dweb.link",  # base2
            "https://7002700221014170434637310537764066371723775207774327464566205514134000113556045464703073645034432.ipfs.dweb.link",  # base8
            "https://92793123896416649578508430956173875066425468388805468715479907750778834469731416946970.ipfs.dweb.link/",  # base10
            "https://f01701220c3c4733ec8affd06cf9e9ff50ffc6bcd2ec85a6170004bb709669c31de94391a.ipfs.dweb.link/",  # base16
            "https://Qmb4sw3sqA7AZsaRZ7vtMwxCduk1ExJL5gVDPcpnP8kxFK.ipfs.dweb.link/",  # base58btc CIDv0
            "http://QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR.ipfs.dweb.link",  # base58btc CIDv0
            "http://bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va.dweb.link",
            "http://QmcNioXSC1bfJj1dcFErhUfyjFzoX2HodkRccsFFVJJvg8.ipns.dweb.link",  # base58btc CIDv0
            "http://bafybeiabc2xofh6tdi6vutusorpumwcikw3hf3st4ecjugo6j52f6xwc6q.dweb.link",  # base32 with missing protocol
            "https://zdj7Wic6KcJAfWz1c9o4M6kq9Lwd5BfbxkVafnrojaaGiSFxM.ipfs.dweb.link",  # base58btc CIDv1
            "https://mAXASIMPEcz7Ir/0Gz56f9Q/8a80uyFphcABLtwlmnDHelDka.ipfs.dweb.link",  # base64
            "http://not-a-cid.ipfs.dweb.link",
            "http://invalid-hostname-.ipns.dweb.link",
            "http://www.bafybeie5gq4jxvzmsym6hjlwxej4rwdoxt7wadqvmmwbqi7r27fclha2va.ipfs.dweb.link",
            "http://not-a-cid-or-valid-hostname-.ipns.dweb.link",
        ],
        "ipns": [
            "http://invalid-hostname-.ipns.dweb.link",
            "https://01011100100000000000100100000010000000000100010010001000000001101100000000001011010111001111011100001111011011011110000110010010011110000111100011011100010111111100111101110101100110111011011101000001100110101011111110001011000001111110000110000111010100101100011010011000111000101000010101010110100001001100110011.ipns.dweb.link",  # base2
            "https://7134400044020004221001540013271734173336062236074334277475654673350146537613017606072454323070502526411463.ipns.dweb.link",  # base8
            "https://7134400044020004221001540013271734173336062236074334277475654673350146537613017606072454323070502526411463.ipns.dweb.link",  # base10
            "https://f01720024080112201b002d73dc3db78649e1e3717f3dd66edd066afe2c1f861d4b1a638a155a1333.ipns.dweb.link",  # base16
            "https://bafzaajaiaejcagyafvz5ypnxqze6dy3rp465m3w5azvp4la7qyouwgtdrikvuezt.ipns.dweb.link",  # base32
            "http://bafybeiabc2xofh6tdi6vutusorpumwcikw3hf3st4ecjugo6j52f6xwc6q.ipns.dweb.link",  # base32
            "https://v05p00908049206o05lptofdngp4u3orhfsutcrmt0plfsb0vgoekm6j3h8alk4pj.ipns.dweb.link",  # base32hex
            "https://Z5azMnuicXMgDMqbtbwJiQHydfF5kzhqYommSLcxq57AXAbA8SFnxoB.ipns.dweb.link",  # base58flickr
            "https://z5AanNVJCxnP3oDACUtS8xaCDPrnpquZbpFZ3pU83Lu8JzQSFnodntY.ipns.dweb.link"  # base58btc CIDv1
            "http://QmcNioXSC1bfJj1dcFErhUfyjFzoX2HodkRccsFFVJJvg8.ipns.dweb.link",  # base58btc CIDv0
            "https://mAXIAJAgBEiB6C43WeEQO+iBUnhM/SS2I/pHzemJnV7m/TKgqgiiJoQ.ipns.dweb.link",  # base64
            "https://uAXIAJAgBEiAbAC1z3D23hknh43F_PdZu3QZq_iwfhh1LGmOKFVoTMw.ipns.dweb.link",  # base64url
        ],
    },
    "path": {
        "ipfs": [
            "/ipfs/72700221014170434637310537764066371723775207774327464566205514134000113556045464703073645034432",  # base8
            "/ipfs/92793123896416649578508430956173875066425468388805468715479907750778834469731416946970",  # base10
            "/ipfs/mAXASIMPEcz7Ir/0Gz56f9Q/8a80uyFphcABLtwlmnDHelDka",  # base64
            "/ipfs/js-ipfs/blob/master/README.md",
            "/ipfs/QmcNioXSC1bfJj1dcFErhUfyjFzoX2HodkRccsFFVJJvg8.ipns.dweb.link",
            "ipfs/QmeWz9YZEeNFXQhHg4PnR5ZiNr5isttgi5n1tc1eD5EfGU"
            "/ipfs/foo/QmeWz9YZEeNFXQhHg4PnR5ZiNr5isttgi5n1tc1eD5EfGU",
            "/foo.bar",
            "/ipfs/mAXASIMPEcz7Ir/0Gz56f9Q/8a80uyFphcABLtwlmnDHelDka",
            "/ipfs/1234",
        ],
        "ipns": [
            "/ipns/7134400044020004221001540013271734173336062236074334277475654673350146537613017606072454323070502526411463",  # base8
            "/ipns/912059270899086145358701227151751949578967872728194642447008830239276889128468550643329311314739",  # base10
            "/ipns/mAXASIMPEcz7Ir/0Gz56f9Q/8a80uyFphcABLtwlmnDHelDka",  # base64
            "/ipns/qmbwqxbekC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR",
            "/ipfs/js-ipfs/blob/master/README.md",
            "/ipns/en-wikipedia--on--ipfs-org/",
            "/foo.bar",
            "/ipns/1234",
            "/ipns/",
        ],
    },
    "native_url": {
        "ipfs": [
            "ipfs://72700221014170434637310537764066371723775207774327464566205514134000113556045464703073645034432",  # base8
            "ipfs://92793123896416649578508430956173875066425468388805468715479907750778834469731416946970",  # base10
            "ipfs://mAXASIMPEcz7Ir/0Gz56f9Q/8a80uyFphcABLtwlmnDHelDka",  # base64
            "ipfs://js-ipfs/blob/master/README.md",
            "ipfs://QmcNioXSC1bfJj1dcFErhUfyjFzoX2HodkRccsFFVJJvg8.ipns.dweb.link",
            "ipfs://foo/QmeWz9YZEeNFXQhHg4PnR5ZiNr5isttgi5n1tc1eD5EfGU",
            "foo://bar",
            "ipfs:/mAXASIMPEcz7Ir/0Gz56f9Q/8a80uyFphcABLtwlmnDHelDka",
            "ipfs://1234",
        ],
        "ipns": [
            "ipns://7134400044020004221001540013271734173336062236074334277475654673350146537613017606072454323070502526411463",  # base8
            "ipns://912059270899086145358701227151751949578967872728194642447008830239276889128468550643329311314739",  # base10
            "ipns://mAXASIMPEcz7Ir/0Gz56f9Q/8a80uyFphcABLtwlmnDHelDka",  # base64
            "ipns://qmbwqxbekC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR",
            "ipfs://js-ipfs/blob/master/README.md",
            "ipns://en-wikipedia--on--ipfs-org/",
            "foo://bar",
            "ipns://1234",
        ],
    },
}
