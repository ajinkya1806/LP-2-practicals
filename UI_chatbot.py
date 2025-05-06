import tkinter as tk
from nltk.chat.util import Chat, reflections

# Chatbot setup
movies = {
    'Interstellar': ['Morning: 10:00 AM', 'Afternoon: 2:00 PM', 'Evening: 6:00 PM'],
    'The Dark Knight': ['Morning: 11:00 AM', 'Afternoon: 3:00 PM', 'Evening: 7:00 PM'],
    'Dune': ['Morning: 9:30 AM', 'Afternoon: 1:30 PM', 'Evening: 5:30 PM']
}

showtime_info = '\n'.join([f"{movie}: {', '.join(times)}" for movie, times in movies.items()])

patterns = [
    (r'\b(hi|hello|hey)\b', ['Hello! How can I assist you today?']),
    (r'\bhow are you\b', ['I am just a bot, but I am always ready to help!']),
    (r'\b(movie|movies)\b', [f"Movies playing:\n{', '.join(movies.keys())}"]),
    (r'\b(ticket|tickets)\b', ['How many tickets would you like to book?']),
    (r'\b(showtime|timing)\b', [f"Showtimes:\n{showtime_info}"]),
    (r'\b(morning|afternoon|evening|night)\b', ['We have showtimes available in the morning, afternoon, and evening.']),
    (r'\bbook tickets\b', ['Sure! Let\'s proceed with booking.']),
    (r'\b(bye|goodbye|exit|quit)\b', ['Thank you! Enjoy your movie.']),
    (r'(.*)', ["I'm not sure I understand. Try asking about movies, tickets, or timings."])
]

movie_bot = Chat(patterns, reflections)

# Booking logic
def book_tickets(movie, tickets, showtime):
    ticket_price = 100
    total = tickets * ticket_price
    return (f"\n✅ Booking confirmed!\n🎬 Movie: {movie}\n🎟️ Tickets: {tickets}\n🕒 Showtime: {showtime}\n"
            f"💵 Total: Rs. {total}\nEnjoy your movie!")

# GUI Setup
def launch_gui():
    def send_message():
        user_msg = entry.get().strip()
        if not user_msg:
            return

        chat_log.insert(tk.END, f"You: {user_msg}\n")
        entry.delete(0, tk.END)

        # Bot response
        response = movie_bot.respond(user_msg)

        # Booking flow
        if 'book tickets' in user_msg.lower():
            def complete_booking():
                m = movie_entry.get()
                t = ticket_entry.get()
                s = showtime_entry.get()

                try:
                    t = int(t)
                    if m not in movies or s not in [x.split(': ')[1] for x in movies[m]]:
                        raise ValueError
                    reply = book_tickets(m, t, s)
                except:
                    reply = "Bot: Invalid booking details. Please try again."
                
                chat_log.insert(tk.END, f"Bot: {reply}\n")
                booking_popup.destroy()

            booking_popup = tk.Toplevel(root)
            booking_popup.title("Book Tickets")

            tk.Label(booking_popup, text="Movie:").grid(row=0, column=0)
            movie_entry = tk.Entry(booking_popup)
            movie_entry.grid(row=0, column=1)

            tk.Label(booking_popup, text="Tickets:").grid(row=1, column=0)
            ticket_entry = tk.Entry(booking_popup)
            ticket_entry.grid(row=1, column=1)

            tk.Label(booking_popup, text="Showtime:").grid(row=2, column=0)
            showtime_entry = tk.Entry(booking_popup)
            showtime_entry.grid(row=2, column=1)

            tk.Button(booking_popup, text="Confirm", command=complete_booking).grid(row=3, columnspan=2)
            return

        chat_log.insert(tk.END, f"Bot: {response}\n")

    # Main window
    global root
    root = tk.Tk()
    root.title("🎥 MovieBot")

    # Chat log
    chat_log = tk.Text(root, height=20, width=60, bg="white")
    chat_log.pack(padx=10, pady=10)
    chat_log.insert(tk.END, "🎥 Welcome to MovieBot! Type 'book tickets' to begin.\n")

    # Entry + Button
    entry_frame = tk.Frame(root)
    entry_frame.pack()

    entry = tk.Entry(entry_frame, width=50)
    entry.pack(side=tk.LEFT, padx=(0, 5))

    send_btn = tk.Button(entry_frame, text="Send", command=send_message)
    send_btn.pack(side=tk.LEFT)

    root.mainloop()

# Run it
launch_gui()
