<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Course</h1>
        <hr><br><br>
        <alert v-if="showMessage" :message="message" />
        <button v-b-modal.search-modal type="button" class="btn btn-success btn-sm">Search</button>
        &nbsp;
        <button type="button" class="btn btn-success btn-sm" @click="getBooks()">Flush</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Course_Name</th>
              <th scope="col">Sec_ID</th>
              <th scope="col">Classroom_Address</th>
              <th scope="col">TIME_SLOT</th>
              <th />
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.course_name }}</td>
              <td>{{ book.sec_id }}</td>
              <td>{{ book.classroom_address }}</td>
              <td>{{ book.time_slot }}</td>
              <td>
                
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    

    <b-modal
      id="search-modal"
      ref="searchBookModal"
      title="Search"
      hide-footer
    >
      <b-form class="w-100" @submit="onSearch" @reset="onReset">
        <b-form-group
          id="form-title-group"
          label="Teacher_ID:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="searchForm.teacher_id"
            type="text"
            required
            placeholder="Enter Teacher_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="Year Semester:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="searchForm.year_semester"
            type="text"
            required
            placeholder="Enter Year Semester"
          />
        </b-form-group>
        
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'
import Alert from '@/components/Alert.vue'

export default {
  components: {
    alert: Alert
  },
  data() {
    return {
      books: [],
      
      message: '',
      showMessage: false,
      
      searchForm: {
        teacher_id: '',
        year_semester: ''
      },
    }
  },
  created() {
    this.getBooks()
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books'
      axios.get(path)
        .then((res) => {
          // this.books = res.data.books
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        })
    },
    addBook(payload) {
      const path = 'http://localhost:5000/books'
      axios.post(path, payload)
        .then(() => {
          this.getBooks()
          this.message = 'Course added!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks()
        })
    },
    searchBook(payload) {
        const path = 'http://localhost:5000/teacourses/search'
        axios.post(path, payload)
            .then((res) => {
                this.books = res.data.books
            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            })
    },
    initForm() {
      
      this.searchForm.student_id = ''
      this.searchForm.year_semester = ''
      
    },
    onSubmit(evt) {
      evt.preventDefault()
      this.$refs.addBookModal.hide()
      // let read = false;
      // if (this.addBookForm.read[0]) read = true;
      const payload = {
        course_id: this.addBookForm.course_id,
        course_name: this.addBookForm.course_name,
        dept_id: this.addBookForm.dept_id,
        course_eng_name: this.addBookForm.course_eng_name,
        credit: this.addBookForm.credit
      }
      this.addBook(payload)
      this.initForm()
    },
    onSearch(evt) {
      evt.preventDefault()
      this.$refs.searchBookModal.hide()
      // let read = false;
      // if (this.addBookForm.read[0]) read = true;
      const payload = {
        teacher_id: this.searchForm.teacher_id,
        year_semester: this.searchForm.year_semester,
      }
      this.searchBook(payload)
      this.initForm()
    },
    onReset(evt) {
      evt.preventDefault()
      this.$refs.addBookModal.hide()
      this.initForm()
    },
    editBook(book) {
      this.editForm = book
    },
    onSubmitUpdate(evt) {
      evt.preventDefault()
      this.$refs.editBookModal.hide()
      // let read = false;
      // if (this.editForm.read[0]) read = true;
      const payload = {
        course_id: this.editForm.course_id,
        course_name: this.editForm.course_name,
        dept_id: this.editForm.dept_id,
        course_eng_name: this.editForm.course_eng_name,
        credit: this.editForm.credit
      }
      this.updateBook(payload, this.editForm.course_id)
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/books/${bookID}`
      axios.put(path, payload)
        .then(() => {
          this.getBooks()
          this.message = 'Course updated!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks()
        })
    },
    onResetUpdate(evt) {
      evt.preventDefault()
      this.$refs.editBookModal.hide()
      this.initForm()
      this.getBooks() // why?
    },
    removeBook(bookID) {
      const path = `http://localhost:5000/books/${bookID}`
      axios.delete(path)
        .then(() => {
          this.getBooks()
          this.message = 'Course removed!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks()
        })
    },
    onDeleteBook(book) {
      this.removeBook(book.course_id)
    }
  }
}
</script>
