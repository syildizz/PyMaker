const promptOutput = document.getElementById("prompt-response");

async function handlePromptSubmit(e) {
    e.preventDefault();

    const promptText = e.target.promptText.value;
    try {
        const response = await fetch('/prompt', {
            method: 'POST', 
            headers: {
                'Content-Type': 'application/json; charset=UTF-8'
            },
            body: JSON.stringify({
                "promptText": promptText
            }) 
        });
        if (response.status !== 200) {
            promptOutput.style.color = "red";
            promptOutput.textContent = "Error: " + (await response.json())['detail'];
        }
        else {
            promptOutput.style.color = "unset";
            promptOutput.textContent = "";
            const decoder = new TextDecoder();
            for await (const chunk of response.body) {
                promptOutput.textContent += decoder.decode(chunk);
            }
        }
    }
    catch (e) {
        promptOutput.style.color = "red";
        promptOutput.textContent = `Error: ${e.message}`;
        throw e;
    }
}

const submitPromptForm = document.getElementById("submit-prompt-form");
submitPromptForm.addEventListener("submit", handlePromptSubmit);
