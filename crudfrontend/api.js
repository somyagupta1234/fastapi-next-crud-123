import useInterCeptor from "./interceptors";

const useApiHelper = () => {
    const axios = useInterCeptor();

    const api = {
        addStudent: (data, params = {}) =>
            axios.post(`${process.env.NEXT_PUBLIC_API_URL}/api/v1/add-student/`, data, params),

        studentDetails: (id, params = {}) =>
            axios.get(`${process.env.NEXT_PUBLIC_API_URL}/api/v1/student-details/${id}`, params),

        studentList: (params = {}) =>
            axios.get(`${process.env.NEXT_PUBLIC_API_URL}/api/v1/student-list/`, params),

        deleteStudent: (id, params = {}) =>
            axios.delete(`${process.env.NEXT_PUBLIC_API_URL}/api/v1/delete-student/${id}`, params),

        updateStudent: (id, data, params = {}) =>
            axios.put(`${process.env.NEXT_PUBLIC_API_URL}/api/v1/student-update/${id}/`, data, params)
    }

    return api;
}
console.log("API URL:", process.env.NEXT_PUBLIC_API_URL);

export default useApiHelper;
