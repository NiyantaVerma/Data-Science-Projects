$(document).ready(function () {
    // Simulate chatbot greeting message
    setTimeout(() => {
        // Getting a random greeting
        const ran = Math.ceil(6*Math.random());
        if (ran===1) {
            appendBotMessage("Welcome to MyAnimal! How can I assist you in finding what you're looking for?");
        }
        else if (ran===2) {
            appendBotMessage("Hello and welcome! Let me assist you in exploring our animals and products.");
        }
        else if (ran===3) {
            appendBotMessage("Namaste! How can I help you find the perfect pet or product today?");
        }
        else if (ran===4) {
            appendBotMessage("Hi! Looking for something special? I can guide you to the perfect choice!");
        }
        else if (ran===5) {
            appendBotMessage("Hi! MyAnimal is our site where you can find pets, livestock, and all the care they need. Would you like to know more?");
        }
        else {
            appendBotMessage("Hi! MyAnimal is our site where you can find pets, livestock, and all the care they need. How can we help you there?");
        }

        // Creting a language selection button
        const buttonHTML = `
        <div class="langSelector">
            <button class="englishLangButton">English</button>
            <button class="hinglishLangButton">Hinglish</button>
        </div>
        `;
        $(".Messages_list").append(buttonHTML);
        // Styling those buttons
        const styleTag = document.createElement("style"); // Create a <style> element
            styleTag.textContent = `
                .langSelector {
                    display: flex;
                    justify-content: flex-start;
                    padding: 10px 0;
                }
                .englishLangButton {
                    display: block;
                    background-color: #28a745;
                    color: white;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 5px;
                    cursor: pointer;
                }
                .englishLangButton:hover {
                    background-color: #218838;
                }
                .hinglishLangButton {
                    background-color: #28a745;
                    color: white;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 5px;
                    cursor: pointer;
                }
                .hinglishLangButton:hover {
                    background-color: #218838;
                }
            `;
            document.head.appendChild(styleTag); // Append the <style> tag to the <head>            
    }, 500);


    // on clicking the English Button

    $(document).on("click", ".englishLangButton", function () {
        // alert("You have chosen English!");
        lang = "en";
        // $(".englishLangButton").remove();
        $(".hinglishLangButton").remove();
    });
    
    $(document).on("click", ".hinglishLangButton", function () {
        // alert("You have chosen Hinglish!");
        lang = "hi-en";
        $(".englishLangButton").remove();
        // $(".hinglishLangButton").remove();
    });

    
    // Function to get bot's response based on the user's input
    async function getBotResponse(userMessage, lang, sessionId, customerId) {
        try {
            // Send the user's message to the backend
            const response = await fetch("http://127.0.0.1:5000/chatbot/response", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    query: userMessage,
                    sessionId: sessionId, // Replace or generate dynamically
                    customerId: customerId, // Replace or generate dynamically
                    lang: lang, // Replace or generate dynamically
                }),
            });

            if (!response.ok) {
                return "Response from server was not ok";
            }

            // Parse the JSON response from the backend
            const data = await response.json();

            // Return the bot's response
            return data.response;
        } catch (error) {
            console.error("Error fetching bot response:", error);
            return "There seems to be an error connecting with bot";
        }
    }


    // Function to append user's message (Right)
    function appendUserMessage(message) {
        $(".Messages_list").append(
            `<div class="msg user">
                <span class="responsText">${message}</span>
            </div>`
        );
        scrollToBottom();
    }

    // Function to append bot's message (Left)
    function appendBotMessage(message) {
        $(".Messages_list").append(
            `<div class="msg">
                <span class="responsText">${message}</span>
            </div>`
        );

        // Check if the message contains the word "apologies"
        if (message === "Apologies, I do not have the info ask something else") {
            const buttonHTML = `
                <div class="personButton">
                    <button class="PTbutton">Resolve Issue</button>
                </div>
                `;
            const styleTag = document.createElement("style"); // Create a <style> element
            styleTag.textContent = `
                .personButton {
                    display: flex;
                    justify-content: flex-start;
                    padding: 10px 0;
                }
                .PTbutton {
                    background-color: #28a745;
                    color: white;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 5px;
                    cursor: pointer;
                }
                .PTbutton:hover {
                    background-color: #218838;
                }
            `;
            $(".Messages_list").append(buttonHTML);
            document.head.appendChild(styleTag); // Append the <style> tag to the <head>            

            // Attach an event listener to the button
        }
        
        scrollToBottom();
    }

    // on clicking the PTbutton
    $(".PTbutton").click(function () {
        alert("Thank you for your feedback! We'll work on resolving your issue.");
    });
    
    // Scroll to the bottom of the chat
    function scrollToBottom() {
        const messagesList = $(".Messages_list");
        messagesList.scrollTop(messagesList.prop("scrollHeight"));
    }
    
    
    // Open chat window with animation
    $("#chatbotIcon").click(function () {
        const chatWindow = $("#chatWindow");
        chatWindow.css("right", "20px"); // Adjust chat window position
        chatWindow.addClass("open"); // Add scaling effect on open
        $(this).hide(); // Hide the chatbot icon after click

    });

    // Close the chat window
    $("#closeButton").click(function () {
        $("#chatWindow").css("right", "-350px");
        $("#chatWindow").removeClass("open"); // Remove scaling effect on close
        $("#chatbotIcon").show(); // Show the chatbot icon when the window closes
    });

    // Send icon click event
    $("#sendButton").click(async function () {
        const userMessage = $("#userInput").val().trim();
        if (userMessage) {
            appendUserMessage(userMessage); // Append user's message
            $("#userInput").val(""); // Clear input field

            // Fetch bot response and append it
            try {
                // Create a function for sessionId, customerId
                sessionId = "sessionId"
                customerId = "customerId"
                const botResponse = await getBotResponse(userMessage, lang, sessionId, customerId); // Wait for the bot's response
                appendBotMessage(botResponse); // Append the bot's response
            } catch (error) {
                console.error("Error handling bot response:", error);
                appendBotMessage("Sorry, something went wrong. Please try again later.");
            }
        }
    });

    // Press Enter to send message
    $("#userInput").keypress(function (event) {
        if (event.which === 13) {
            $("#sendButton").click();
        }
    });
    
});
