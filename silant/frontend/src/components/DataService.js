import axios from "axios";

export default class DataService {

    static async getAll() {
        let context = []
        let verboseName = []
        const responce = await axios.get('http://127.0.0.1:8000/api/index/')
        return responce;
    }
}