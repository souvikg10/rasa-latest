from rasa_core_sdk import Action


class ActionCardLost(Action):
   def name(self):
      # type: () -> Text
      return "card_lost"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        dispatcher.utter_template("utter_card_retrieval_confirmed", tracker)
      