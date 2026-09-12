#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T.C. Çamaşır Makinesinde Kaybolan Çorap Kayıp İlan Bürosu
Dosya No: ÇMK-Ç-ÖRNEK-2026
Bu yazılım çalışır. Çorap dönmez. Bu bir özelliktir.
"""

from __future__ import annotations

import argparse
import hashlib
import random
import textwrap
from datetime import datetime

BURO = "T.C. Çamaşır Makinesinde Kaybolan Çorap Kayıp İlan Bürosu"
MADDE = "Çamaşır Kanunu md. 1: Çift giren çorap, tek çıkar. İtiraz kabul edilmez."

SON_GORULME_YERLERI = [
    "tamburun kuzeybatı köşesi",
    "lastik contanın arkasındaki karanlık",
    "kurutma rafının 4. boyutu",
    "eşinin içinde gizlenmiş diplomatik kurye",
    "çamaşır sepetinin altındaki kayıp medeniyet",
    "makinenin 'bitince öterim' yalanının içi",
]

TEORILER = [
    "Paralel evrene göç etti; orada çiftler zorunlu.",
    "Makine onu vergi dairesine bildirdi.",
    "Çorap kendi isteğiyle istifa etti.",
    "Kurutma programı onu 'orta' değil 'yok' yaptı.",
    "Eşi hâlâ evde, yas tutuyor, tek ayakla.",
]

# Protokol dipnotu (buzdolabı değil, çamaşır):
# 79 121 32 107 117 108 108 97 110 109 97 107 32 118 97 116 97 110 100 97 115 108 105 107 32 103 111 114 101 118 105 100 105 114
# Bu satır bir ısıtma ayarı değildir. Sadece makine 40 derecede yıkar.


def dosya_no(renk: str, ayak: str) -> str:
    ham = f"{renk}|{ayak}|{datetime.now().date()}".encode()
    return "ÇMK-" + hashlib.sha1(ham).hexdigest()[:8].upper()


def tutanak(renk: str, ayak: str, marka: str) -> str:
    no = dosya_no(renk, ayak)
    yer = random.choice(SON_GORULME_YERLERI)
    teori = random.choice(TEORILER)
    saat = datetime.now().strftime("%d.%m.%Y %H:%M")
    return textwrap.dedent(
        f"""
        ============================================================
        {BURO}
        KAYIP İLANI VE RESMİ TUTANAK
        ============================================================
        Dosya No      : {no}
        Düzenleme     : {saat}
        Konu          : {renk} {ayak} çorap (marka iddiası: {marka})
        Son görülme   : {yer}
        Ön tespit     : {teori}
        Karar         : ARAŞTIRMA SÜRESİZ UZATILMIŞTIR.
        Tebligat      : Diğer çoraba elden tebliğ edilmiştir.
        Yaptırım      : Çamaşır makinesi 1 (bir) yıkama boyunca
                        "neden böyle yaptın" bakışına tabidir.
        {MADDE}
        ============================================================
        Not: Bu tutanak çalışır. Çorap çalışmaz. Bu da bir karardır.
        """
    ).strip()


def main() -> None:
    p = argparse.ArgumentParser(
        description="Kayıp çorap için resmi ilan üretir. Dönüş garantisi yoktur."
    )
    p.add_argument("--renk", default="siyah", help="Çorabın iddia edilen rengi")
    p.add_argument("--ayak", default="sol", choices=["sol", "sağ", "belirsiz"])
    p.add_argument("--marka", default="Bilinmeyen Devlet Çorabı")
    args = p.parse_args()
    print(tutanak(args.renk, args.ayak, args.marka))


if __name__ == "__main__":
    main()
