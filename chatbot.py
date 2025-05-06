from nltk.chat.util import Chat, reflections

# Define available movies and their showtimes
movies = {
    'Interstellar': ['Morning: 10:00 AM', 'Afternoon: 2:00 PM', 'Evening: 6:00 PM'],
    'The Dark Knight': ['Morning: 11:00 AM', 'Afternoon: 3:00 PM', 'Evening: 7:00 PM'],
    'Dune': ['Morning: 9:30 AM', 'Afternoon: 1:30 PM', 'Evening: 5:30 PM']
}

# Preformatted showtimes for better readability
# showtime_info = '\n'.join([f"{movie}: {', '.join(times)}" for movie, times in movies.items()])
showtime_info = ""
for movie, times in movies.items():
    showtime_info += f"{movie}: {', '.join(times)}\n"


# Define chatbot patterns and responses
patterns = [
    (r'\b(hi|hello|hey)\b', 
     ['Hello! How can I assist you today?', 'Hi there! Want to book a movie ticket?', 'Greetings!']),
    
    (r'\bhow are you\b', 
     ['I am just a bot, but I am always ready to help!', 'Doing great! What movie would you like to watch?']),
    
    (r'\b(movie|movies)\b', 
     [f"Here are the movies currently playing:\n{', '.join(movies.keys())}"]),
    
    (r'\b(ticket|tickets)\b', 
     ['How many tickets would you like to book?']),
    
    (r'\b(showtime|showtimes|timing|timings)\b', 
     [f"Here are the showtimes for the available movies:\n{showtime_info}"]),
    
    (r'\b(morning|afternoon|evening|night)\b', 
     ['We have showtimes available in the morning, afternoon, and evening. Please specify your preferred movie and time.']),
    
    (r'\bbook tickets\b', 
     ['Sure! Let\'s proceed with booking.']),
    
    (r'\b(bye|goodbye|exit|quit)\b', 
     ['Thank you for using the MovieBot. Enjoy your show!', 'Goodbye! See you again soon.']),
    
    (r'(.*)', 
     ["I'm sorry, I didn't quite get that. Can you rephrase or ask about movies, tickets, or showtimes?"])
]

# Initialize the chatbot
movie_bot = Chat(patterns, reflections)

# Booking logic
def book_tickets(movie, tickets, showtime):
    ticket_price = 100  # Fixed ticket price
    total = tickets * ticket_price
    return (f"\n Booking confirmed!\n Movie: {movie}\n Tickets: {tickets}\n Showtime: {showtime}\n"
            f" Total Amount: Rs. {total}\nEnjoy your movie!")

# Main interaction loop
def main():
    print("\n Welcome to MovieBot!")
    print("Type 'book tickets' to start booking or 'bye' to exit.")

    while True:
        user_input = input("You: ").strip()
        response = movie_bot.respond(user_input)
        print("Bot:", response)

        # If the user wants to book tickets
        if 'book tickets' in user_input.lower():
            movie = input("🎬 Which movie would you like to watch? : ").strip()
            if movie not in movies:
                print("Bot: Sorry, that movie is not available.")
                continue

            try:
                tickets = int(input("How many tickets do you want? : "))
                if tickets <= 0:
                    print("Bot: Please enter a valid number of tickets.")
                    continue
            except ValueError:
                print("Bot: Please enter a numeric value for tickets.")
                continue

            print(f"Available showtimes for {movie}: {', '.join(movies[movie])}")
            showtime = input(" Choose a showtime from the above list: ").strip()
            if showtime not in [s.split(': ')[1] for s in movies[movie]]:
                print("Bot: That showtime isn't available for this movie.")
                continue

            confirmation = book_tickets(movie, tickets, showtime)
            print("Bot:", confirmation)

        # Exit condition
        if any(word in user_input.lower() for word in ['bye', 'goodbye', 'exit', 'quit']):
            break

# Run the chatbot
main()
