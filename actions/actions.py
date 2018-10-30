from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class ActionSetTicket(Action):
   def name(self):
      # type: () -> Text
      return "card_lost"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        dispatcher.utter_message("I have contacted the team. We will issue you a new card really soon")

