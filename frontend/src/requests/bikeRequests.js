export const fetchBikes = async () => {
    try {
        const response = await fetch('http://127.0.0.1:5000/bikes');
        const bikes = await response.json();
        return bikes
    } catch (error) {
        console.log(error)
    }
}