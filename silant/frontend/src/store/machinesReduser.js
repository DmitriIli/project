const defaultState = {
    machines:[],
}

export const machinesReduser = (state = defaultState, action) => {
    switch (action.type) {
        case "GETMACHINES":
            return { ...state, machines:[ ...state.machines, action.payload ]}
        default:
            return state
    }
}