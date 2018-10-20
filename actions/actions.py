from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class ActionSetTicket(Action):
   def name(self):
      # type: () -> Text
      return "set_ticket_number"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        Number = tracker.get_slot("number")
        return [SlotSet("Ticket", Number)]

class ActionRetrieveTicket(Action):
   def name(self):
      # type: () -> Text
      return "retrieve_ticket_status"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        dispatcher.utter_message("Votre ticket n'est pas disponible")