HEADERS = [
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",'"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",'"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',"macOS"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",'"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",'"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',"macOS"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/6.6.0 Chrome/112.0.5615.213 Safari/537.36",'"Not:A-Brand";v="99", "Chromium";v="112"',"Linux"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',"Linux"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",'"Not=A?Brand";v="99", "Chromium";v="118"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",'"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",'"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',"macOS"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',"macOS"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',"Windows"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",'"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',"Linux"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',"macOS"),
    ("Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2887.77 Safari/537.36",'"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",'"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',"macOS"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",'"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',"Linux"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",'"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',"Linux"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",'"Not.A/Brand";v="8", "Chromium";v="114"',"Windows"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",'"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',"Linux"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",'"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',"macOS"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Iron Safari/537.36",'"Chromium";v="109", "Not_A Brand";v="99"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",'"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61",'"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Avast/118.0.0.0",'"Chromium";v="118", "Avast Secure Browser";v="118", "Not=A?Brand";v="99"',"Windows"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",'"Not.A/Brand";v="8", "Chromium";v="114"',"Linux"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",'" Not;A Brand";v="99", "Google Chrome";v="89", "Chromium";v="89"',"Windows"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61",'"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',"Linux"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",'"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',"macOS"),
    ("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2863.41 Safari/537.36",'"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',"macOS"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",'"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',"Windows"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",'"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',"Linux"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76",'"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",'"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",'" Not;A Brand";v="99", "Google Chrome";v="88", "Chromium";v="88"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",'"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',"macOS"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54",'"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',"Windows"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',"Linux"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",'" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",'"HeadlessChrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',"Linux"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",'"Not:A-Brand";v="99", "Chromium";v="112"',"Linux"),
    ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Atom/4.0.0.141 Safari/537.36",'" Not;A Brand";v="99", "Google Chrome";v="75", "Chromium";v="75"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",'" Not;A Brand";v="99", "Google Chrome";v="80", "Chromium";v="80"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",'" Not;A Brand";v="99", "Google Chrome";v="88", "Chromium";v="88"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 AVG/118.0.0.0",'"Chromium";v="118", "AVG Secure Browser";v="118", "Not=A?Brand";v="99"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",'" Not;A Brand";v="99", "Google Chrome";v="88", "Chromium";v="88"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 uacq",'"Google Chrome";v="113", "Chromium";v="113", "Not=A?Brand";v="24"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",'" Not;A Brand";v="99", "Google Chrome";v="74", "Chromium";v="74"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60",'"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',"Windows"),
    ("Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",'" Not;A Brand";v="99", "Google Chrome";v="67", "Chromium";v="67"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",'" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",'"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',"macOS"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",'"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',"macOS"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36",'"Chromium";v="15", "Not.A/Brand";v="8"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",'"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',"Windows"),
    ("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2761.55 Safari/537.36",'"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',"Windows"),
    ("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",'" Not;A Brand";v="99", "Google Chrome";v="89", "Chromium";v="89"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46",'"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',"Windows"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',"Linux"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 (Chromium GOST)",'"Chromium";v="107", "Not=A?Brand";v="24"',"Windows"),
    ("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",'" Not;A Brand";v="99", "Google Chrome";v="72", "Chromium";v="72"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',"macOS"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",'" Not;A Brand";v="99", "Google Chrome";v="79", "Chromium";v="79"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",'" Not;A Brand";v="99", "Google Chrome";v="80", "Chromium";v="80"',"Windows"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.15 Safari/537.36",'"(Not(A:Brand";v="8", "Chromium";v="101"',"Linux"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69",'"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69",'"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',"macOS"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",'"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',"macOS"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57",'"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',"macOS"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188",'"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69",'"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.106 Safari/537.36",'"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",'"Chromium";v="107", "Not=A?Brand";v="24"',"macOS"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50",'"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',"macOS"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61",'"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',"macOS"),
    ("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",'" Not;A Brand";v="99", "Google Chrome";v="79", "Chromium";v="79"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76",'"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',"macOS"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",'"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',"macOS"),
    ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36",'"Not.A/Brand";v="8", "Chromium";v="114"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36",'"Google Chrome";v="119", "Chromium";v="119", ";Not A Brand";v="99"',"Windows"),
    ("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2964.70 Safari/537.36",'"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',"Windows"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',"Linux"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.5150.0 Iron Safari/537.36",'"(Not(A:Brand";v="8", "Chromium";v="101"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43",'"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",'" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',"macOS"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',"Windows"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",'"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',"Linux"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57",'"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",'"Chromium";v="21", " Not;A Brand";v="99"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",'"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',"macOS"),
    ("Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.140",'"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',"Windows"),
    ("Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36",'"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',"Windows"),
    ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.140",'"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Avast/117.0.0.0",'"Avast Secure Browser";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",'" Not;A Brand";v="99", "Google Chrome";v="89", "Chromium";v="89"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",'" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",'"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',"macOS"),
    ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',"Windows"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',"macOS"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.34",'"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',"Windows"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",'" Not;A Brand";v="99", "Google Chrome";v="89", "Chromium";v="89"',"Windows")
]