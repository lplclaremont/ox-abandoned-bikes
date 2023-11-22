export const fetchLocations = async () => {
    try {
        const response = await fetch('http://127.0.0.1:5000/locations');
        const locations = await response.json();
        return locations;
    } catch (error) {
        console.log(error)
    }
}