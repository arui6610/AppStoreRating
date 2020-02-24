# AppStoreRating
Apple官方有提供一个API可以用来获取App的评论数据，这个API最多可以获取500条数据，每页最多50条，最多10页。

示例链接如下：

https://itunes.apple.com/cn/rss/customerreviews/page=1/id=414478124/sortby=mostrecent/json

获取的数据中发现评论中没有评论时间信息等。这显然不满足需求。那么接着搞。

https://itunes.apple.com/cn/rss/customerreviews/page=1/id=414478124/sortby=mostrecent/xml

惊喜的发现xml格式的数据中有评论时间。妥。

然后按照步骤：

1. 获取xml数据
2. xml转json数据
3. 解析json
4. 提取数据（评论id，时间，用户，标题，内容，评分，版本）

到了这一步。基本已经完成的需求。成功获取应用在App Store的用户评论数据。

那么问题来了，我们的应用是发布全球市场的，如何获取其他国家的评论数据呢？

在上面的url中发现有cn，这表示我们拿到的是中国区的数据。那么其他的国家的数据是不是修改区域码？

那么将链接中的cn替换为us看看。

https://itunes.apple.com/us/rss/customerreviews/page=1/id=414478124/sortby=mostrecent/xml

果然获取到了美国区的数据。有一个关于应用的id的问题，发现不管哪个区同一个应用都是同一个id。猜测这个和你打包上传itnues store的时候生成的应用id有关。

到了这一步，成功获取到了中国区，美国区的用户评论数据。

那么剩下的工作就是拿到App Stor支持的其他区下的所有数据。

如下列出了App Store支持的国家和区域：

```json
{
        " Armenia":"am",
        " Bahrain":"bh",
        " البحرين": "bh-ar",
        " Botswana": "bw",
        " Cameroun": "cm",
        " République Centrafricaine": "cf",
        " Côte d'Ivoire": "ci",
        " Egypt": "eg",
        " مصر": "eg-ar",
        " Guinea-Bissau": "gw",
        " Guinée": "gn",
        " Guinée Equatoriale": "gq",
        " India": "in",
        " Israel": "il",
        " Jordan": "jo",
        " الأردن": "jo-ar",
        " Kenya": "ke",
        " Kuwait": "kw",
        " الكويت": "kw-ar",
        " Madagascar": "mg",
        " Mali": "ml",
        " Maroc": "ma",
        " Maurice": "mu",
        " Mozambique": "mz",
        " Niger": "ne",
        " Nigeria": "ng",
        " Oman": "om",
        " عُمان": "om-ar",
        " Qatar": "qa",
        " قطر": "qa-ar",
        " Saudi Arabia": "sa",
        " المملكة العربية السعودية": "sa-ar",
        " Sénégal": "sn",
        " South Africa": "za",
        " Tunisie": "tn",
        " Uganda": "ug",
        " United Arab Emirates": "ae",
        " الإمارات العربية المتحدة": "ae-ar",
        " Australia": "au",
        " 中国大陆": "cn",
        " Hong Kong (English)": "hk/en",
        " 香港": "hk",
        " Indonesia": "id",
        " 日本": "jp",
        " 대한민국": "kr",
        " 澳門": "mo",
        " Malaysia": "my",
        " New Zealand": "nz",
        " Philippines": "ph",
        " Singapore": "sg",
        " 台灣": "tw",
        " ไทย": "th",
        " Vietnam": "vn",
        " België": "benl",
        " Belgique": "befr",
        " България": "bg",
        " Česko": "cz",
        " Danmark": "dk",
        " Deutschland": "de",
        " Eesti": "ee",
        " España": "es",
        " France": "fr",
        " Ελλάδα": "gr",
        " Hrvatska": "hr",
        " Ireland": "ie",
        " Italia": "it",
        " Latvija": "lv",
        " Liechtenstein": "li",
        " Lietuva": "lt",
        " Luxembourg": "lu",
        " Magyarország": "hu",
        " Malta": "mt",
        " Moldova": "md",
        " Montenegro": "me",
        " Nederland": "nl",
        " North Macedonia": "mk",
        " Norge": "no",
        " Österreich": "at",
        " Polska": "pl",
        " Portugal": "pt",
        " România": "ro",
        " Россия": "ru",
        " Slovensko": "sk",
        " Slovenia": "si",
        " Schweiz": "chde",
        " Suisse": "chfr",
        " Suomi": "fi",
        " Sverige": "se",
        " Türkiye": "tr",
        " UK": "uk",
        " Anguilla": "lae",
        " Antigua & Barbuda": "lae",
        " Argentina": "la",
        " Barbados": "lae",
        " Belize": "lae",
        " Bermuda": "lae",
        " Bolivia": "la",
        " Brasil": "br",
        " British Virgin Islands": "lae",
        " Cayman Islands": "lae",
        " Chile": "cl",
        " Colombia": "co",
        " Costa Rica": "la",
        " Dominica": "lae",
        " República Dominicana": "la",
        " Ecuador": "la",
        " El Salvador": "la",
        " Grenada": "lae",
        " Guatemala": "la",
        " Guyana": "lae",
        " Honduras": "la",
        " Jamaica": "lae",
        " México": "mx",
        " Montserrat": "lae",
        " Nicaragua": "la",
        " Panamá": "la",
        " Paraguay": "la",
        " Perú": "la",
        " St. Kitts & Nevis": "lae",
        " St. Lucia": "lae",
        " St. Vincent & The Grenadines": "lae",
        " Suriname": "lae",
        " The Bahamas": "lae",
        " Trinidad & Tobago": "lae",
        " Turks & Caicos": "lae",
        " Uruguay": "la",
        " Venezuela": "la",
        " América Latina y el Caribe (Español)": "la",
        " Latin America and the Caribbean (English)": "lae",
        " Canada (English)": "ca",
        " Canada (Français)": "ca/fr",
        " Puerto Rico (English)": "lae",
        " Puerto Rico (Español)": "la",
        " United States": "us",
    }
```
