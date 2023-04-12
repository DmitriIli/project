import axios from "axios";

export default class DataService {

    static async getAll() {
        let context = []
        let verboseName = []
        const responce = await axios.get('http://127.0.0.1:8000/api/index/')
            .then(responce => {
                context = responce.data.context;
                console.log(context)
                verboseName = responce.data.versboseName;
            })
            .catch((e) => {
                console.log(e);
            });
        
        return context, verboseName;
    }
}