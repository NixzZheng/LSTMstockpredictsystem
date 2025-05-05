import { defineStore} from 'pinia'
import axios from 'axios'

export const useStockStore = defineStore('stock', {
    actions: {
        async fetchStockData(code) {
            const response = await axios.get('/api/stock/${code}')
            return response.data
        }
    }
})