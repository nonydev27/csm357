# Human Limits and Performance in Interface Design
*Format: Written Summary*

## Human Limits and Visual Variables
The manipulation of visual variables—specifically contrast, size, and brightness—demonstrated direct impacts on human cognitive and motor performance. Under the "Low Contrast" and "Small Size" conditions, the identification task took noticeably longer. Participants exhibited signs of increased cognitive load, requiring more time to parse the ambiguous Necker Cube illusion.

This mirrors real-world system failures. For instance, early ATMs placed outdoors often featured screens with low luminance and poor contrast. When hit by direct sunlight (competing brightness), the contrast ratio dropped below the threshold of human visual perception, causing delayed task completion, eye strain, and user errors. Similarly, modern websites using light-gray text on white backgrounds sacrifice legibility for aesthetics, actively hindering reading speed and comprehension for users due to limitations in human visual acuity.

## Applying Fitts' Law
Fitts' Law predicts that the time required to rapidly move to a target area is a function of the ratio between the distance to the target (D) and the width of the target (W), expressed as $MT = a + b \log_2(2D/W)$.

The data recorded in the `results.csv` file aligns directly with this predictive model. When the interface size was set to "Large," the generated target buttons possessed a wider clickable surface area (larger W). Consequently, the movement time (MT) recorded from the moment the user clicked "Start" to hitting the "Target" decreased significantly. Conversely, when the target spawned at a further pixel distance (larger D) under the "Small" size condition, participants required more corrective cursor movements at the end of their trajectory (the deceleration phase), significantly increasing the total time taken.

## Design for Diversity
Standardizing interface designs based on average capabilities alienates a massive segment of the user population.

*   **Color-Blind Users:** If an interface relies solely on color hues to convey information (e.g., a red target button on a green background), deuteranopic users will struggle to differentiate the elements. The application accounts for this by allowing the tester to adjust luminance contrast (High/Medium/Low), proving that strong contrast in brightness is more inclusive than relying on hue differences alone.
*   **Elderly Users:** Due to presbyopia (loss of eye lens elasticity) and decreased pupillary response, older adults require much more light to see clearly and struggle with small focal points. The "Small Size" and "Low Brightness" conditions would disproportionately spike their task completion times and drastically lower their "Ease of Use" ratings compared to younger users. Flexible scaling accommodates this demographic.

## Recognition vs Recall
A core heuristic of Human-Computer Interaction is minimizing the user's memory load by prioritizing recognition over recall. The testing application succeeds in this by utilizing persistent, clearly labeled control panels. Instead of forcing the experimenter to remember keyboard shortcuts or type terminal commands to change testing states (recall), the interface provides radio buttons and sliders mapping directly to visual variables (recognition). In the identification task, the system explicitly prompts the user via a dialog box, guiding them through the workflow rather than requiring them to remember the sequential steps of the experiment.