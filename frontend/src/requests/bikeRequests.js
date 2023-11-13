export const fetchBikes = async () => {
    try {
        const response = await fetch('http://127.0.0.1:5000/bikes');
        const bikes = await response.json();
        return bikes
    } catch (error) {
        console.log(error);
    }
}

export const postBike = async (data) => {
    try {
        const response = fetch('http://127.0.0.1:5000/bikes', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data)
        });
        
        result = await response.json();
        console.log("Success:", result)
    } catch (error) {
        console.log(error);
    }
}