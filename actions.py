from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.events import UserUtteranceReverted
from rasa_core_sdk.events import AllSlotsReset
from rasa_core_sdk.events import Restarted

import requests
import json
import feedparser

# Ham lay ket qua so xo va tra ve. Ten ham la action_get_lottery
class action_get_lottery(Action):
	def name(self):
            # Doan nay khai bao giong het ten ham ben tren la okie
		    return 'action_get_lottery'
	def run(self, dispatcher, tracker, domain):
            # Khai bao dia chi luu tru ket qua so xo. O day lam vi du nen minh lay ket qua SX Mien Bac
            url = 'https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss'
            # Tien hanh lay thong tin tu URL
            feed_cnt = feedparser.parse(url)
            # Lay ket qua so xo moi nhat
            first_node = feed_cnt['entries']
            # Lay thong tin ve ngay va chi tiet cac giai
            return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']
            # Tra ve cho nguoi dung
            dispatcher.utter_message(return_msg)
            return []