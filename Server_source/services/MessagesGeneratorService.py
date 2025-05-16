import pandas as pd
import random

class MessagesGeneratorService():

    def __init__(self):
        # Number of messages
        self.total_messages = 500
        self.flood_count = self.total_messages // 3  # approximately 1/3
        self.non_flood_count = self.total_messages - self.flood_count

    def generate_flood_message(self):
        times = ["5:00 today", "12:00", "6:30 this morning", "18:00 last night", "3:15 AM"]
        locations = ["Wistula river in Dobrzannsk city", "our little town", "the northern valley", "the downtown area", "the old district"]
        events = ["dam collapsed", "levee broke", "river overflowed", "storm surge hit", "flash flood occurred"]
        templates = [
            f"The dam on {random.choice(locations)} have just {random.choice(events)}.",
            f"My house is in water. We have a flooding in {random.choice(locations)}.",
            f"The water showed up at {random.choice(times)} and now {random.choice(locations)} is submerged.",
            f"{random.choice(locations).capitalize()} is underwater after the {random.choice(events)} at {random.choice(times)}."
        ]
        msg = random.choice(templates)
        if random.random() < 0.5:
            msg += " " + random.choice([
                "It is a dangerous situation.",
                "Rescue teams are on their way.",
                "Many homes are affected."
            ])
        return msg

    def generate_non_flood_message(self):
        topics = [
            "book recommendation", "daily reflection", "tech tip", "motivational quote",
            "cooking advice", "movie suggestion", "exercise routine", "travel plan"
        ]
        topic = random.choice(topics)
        if topic == "book recommendation":
            return random.choice([
                "I advice everyone to read '1984' before it becomes outdated.",
                "If you love mysteries, 'The Girl with the Dragon Tattoo' is a must-read."
            ])
        if topic == "daily reflection":
            return random.choice([
                "It is sad to watch how our city is changing over time.",
                "I remember the park as a child; now it looks completely different."
            ])
        if topic == "tech tip":
            return random.choice([
                "Restarting your router can often fix internet issues.",
                "Use a password manager to keep your accounts secure."
            ])
        if topic == "motivational quote":
            return random.choice([
                "Believe in yourself and all that you are capable of.",
                "Every journey begins with a single step."
            ])
        if topic == "cooking advice":
            return random.choice([
                "Add a pinch of salt to bring out the sweetness in tomatoes.",
                "Let the meat rest before slicing to keep it juicy."
            ])
        if topic == "movie suggestion":
            return random.choice([
                "If you're in the mood for a thriller, watch 'Se7en'.",
                "The animated film 'Coco' is a beautiful story about family."
            ])
        if topic == "exercise routine":
            return random.choice([
                "Try 10 push-ups, 20 squats, and a 1-minute plank every morning.",
                "A brisk 30-minute walk can boost your energy levels."
            ])
        if topic == "travel plan":
            return random.choice([
                "Plan a weekend trip to the mountains for some fresh air.",
                "Exploring local museums can be a great way to spend a day."
            ])
        
    def generate_messeges(self,path_to_input_folder:str) -> None:
        messages = []
        for _ in range(self.flood_count):
            messages.append((1, self.generate_flood_message()))
        for _ in range(self.non_flood_count):
            messages.append((0, self.generate_non_flood_message()))

        # Shuffle messages
        random.shuffle(messages)

        # Create DataFrame
        df = pd.DataFrame(messages, columns=['is_about_flood', 'message'])

        # Save to CSV
        path_to_save = path_to_input_folder + '/test_messages.csv'
        df.to_csv(path_to_save, sep=';', index=False, header=['is_about_flood', 'message'], quoting=1)