# Calls Music 2 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from ..helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hai {message.from_user.first_name}!</b>

Gua bot mussic santai, bot yang di buat untuk menemani waktu santai anda di vcg.
Jangan lupa masukin juga assisten nya @Assistenmussicsantai_bot Gk tau cara memakainya? Hubungi kontak pembuat!  

Perintah yang mendukung saat ini adalah:

/play - Putar file/link audio yang di reply atau video YouTube.
/pause - Jeda pemutaran audio/lagu.
/resume - Lanjutkan pemutaran audio/lagu.
/skip - Lewati pemutaran audio/lagu.
/stop - Bersihkan antrian dan hapus bot pengguna dari panggilan.
/channel - Setel saluran obrolan (setelah disetel, bot akan diputar di panggilan saluran itu).
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Pembuat 📌", url="https://t.me/gksukaribett"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Grup 📌", url="https://t.me/wavyheartt"
                    ),
                    InlineKeyboardButton(
                        "Channel 📌", url="https://t.me/calonsinger"
                    )
                ]
            ]
        )
    )
