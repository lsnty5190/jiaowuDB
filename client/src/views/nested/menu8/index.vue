<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>STUDENT</h1>
        <hr><br><br>
        <alert v-if="showMessage" :message="message" />
        <button v-b-modal.book-modal type="button" class="btn btn-success btn-sm">Add</button>
        &nbsp;
        <button v-b-modal.search-modal type="button" class="btn btn-success btn-sm">Search</button>
        &nbsp;
        <button type="button" class="btn btn-success btn-sm" @click="getBooks()">Flush</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Teacher_ID</th>
              <th scope="col">Course_ID</th>
              <th scope="col">Sec_ID</th>
              <th scope="col">Year Semester</th>
              <th />
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.teacher_id }}</td>
              <td>{{ book.course_id }}</td>
              <td>{{ book.sec_id }}</td>
              <td>{{ book.year_semester }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    v-b-modal.book-update-modal
                    type="button"
                    class="btn btn-warning btn-sm"
                    @click="editBook(book)"
                  >
                    Update
                  </button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="onDeleteBook(book)"
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal
      id="book-modal"
      ref="addBookModal"
      title="Add a new student"
      hide-footer
    >
      <b-form class="w-100" @submit="onSubmit" @reset="onReset">
        <b-form-group
          id="form-title-group"
          label="teacher_id:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="addBookForm.teacher_id"
            type="text"
            required
            placeholder="Enter Teacher_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="Course ID:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="addBookForm.course_id"
            type="text"
            required
            placeholder="Enter Course ID"
          />
        </b-form-group>
        <b-form-group
          id="form-dept-group"
          label="Sec_ID:"
          label-for="form-dept-input"
        >
          <b-form-input
            id="form-dept-input"
            v-model="addBookForm.sec_id"
            type="text"
            required
            placeholder="Enter Sec_id"
          />
        </b-form-group>
        <b-form-group
          id="form-cedit-group"
          label="Year Semester:"
          label-for="form-credit-input"
        >
          <b-form-input
            id="form-credit-input"
            v-model="addBookForm.year_semester"
            type="text"
            required
            placeholder="Enter Year Semester"
          />
        </b-form-group>
        
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal
      id="book-update-modal"
      ref="editBookModal"
      title="Update"
      hide-footer
    >
      <b-form class="w-100" @submit="onSubmitUpdate" @reset="onResetUpdate">
         <b-form-group
          id="form-title-group"
          label="teacher_id:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="editForm.teacher_id"
            type="text"
            required
            placeholder="Enter Teacher_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="Course ID:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="editForm.course_id"
            type="text"
            required
            placeholder="Enter Course ID"
          />
        </b-form-group>
        <b-form-group
          id="form-dept-group"
          label="Sec_ID:"
          label-for="form-dept-input"
        >
          <b-form-input
            id="form-dept-input"
            v-model="editForm.sec_id"
            type="text"
            required
            placeholder="Enter Sec_id"
          />
        </b-form-group>
        <b-form-group
          id="form-cedit-group"
          label="Year Semester:"
          label-for="form-credit-input"
        >
          <b-form-input
            id="form-credit-input"
            v-model="editForm.year_semester"
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

    <b-modal
      id="search-modal"
      ref="searchBookModal"
      title="Search student"
      hide-footer
    >
      <b-form class="w-100" @submit="onSearch" @reset="onReset">
         <b-form-group
          id="form-title-group"
          label="teacher_id:"
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
          label="Course ID:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="searchForm.course_id"
            type="text"
            required
            placeholder="Enter Course ID"
          />
        </b-form-group>
        <b-form-group
          id="form-dept-group"
          label="Sec_ID:"
          label-for="form-dept-input"
        >
          <b-form-input
            id="form-dept-input"
            v-model="searchForm.sec_id"
            type="text"
            required
            placeholder="Enter Sec_id"
          />
        </b-form-group>
        <b-form-group
          id="form-cedit-group"
          label="Year Semester:"
          label-for="form-credit-input"
        >
          <b-form-input
            id="form-credit-input"
            v-model="searchForm.year_semester"
            type="text"
            required
            placeholder="Enter Year Semester"
          />
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
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
      addBookForm: {
        teacher_id: '',
        course_id: '',
        sec_id: '',
        year_semester: ''
      },
      message: '',
      showMessage: false,
      editForm: {
        teacher_id: '',
        course_id: '',
        sec_id: '',
        year_semester: ''
      },
      searchForm: {
        teacher_id: '',
        course_id: '',
        sec_id: '',
        year_semester: ''
      }
    }
  },
  created() {
    this.getBooks()
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/teach'
      axios.get(path)
        .then((res) => {
          this.books = res.data.books
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        })
    },
    addBook(payload) {
      const path = 'http://localhost:5000/teach'
      axios.post(path, payload)
        .then(() => {
          this.getBooks()
          this.message = 'Student added!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks()
        })
    },
    searchBook(payload) {
        const path = 'http://localhost:5000/teach/search'
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
      this.addBookForm.teacher_id = ''
      this.addBookForm.course_id = ''
      this.addBookForm.sec_id = ''
      this.addBookForm.year_semester = ''

      this.editForm.teacher_id = ''
      this.editForm.course_id = ''
      this.editForm.sec_id = ''
      this.editForm.year_semester = ''

      this.searchForm.teacher_id = ''
      this.searchForm.course_id = ''
      this.searchForm.sec_id = ''
      this.searchForm.year_semester = ''
    },
    onSubmit(evt) {
      evt.preventDefault()
      this.$refs.addBookModal.hide()
      // let read = false;
      // if (this.addBookForm.read[0]) read = true;
      const payload = {
        teacher_id: this.addBookForm.teacher_id,
        course_id: this.addBookForm.course_id,
        sec_id: this.addBookForm.sec_id,
        year_semester: this.addBookForm.year_semester
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
        course_id: this.searchForm.course_id,
        sec_id: this.searchForm.sec_id,
        year_semester: this.searchForm.year_semester
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
        teacher_id: this.editForm.teacher_id,
        course_id: this.editForm.course_id,
        sec_id: this.editForm.sec_id,
        year_semester: this.editForm.year_semester
      }
      this.updateBook(payload, this.editForm.teacher_id)
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/teach/${bookID}`
      axios.put(path, payload)
        .then(() => {
          this.getBooks()
          this.message = 'Teaching updated!'
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
      const path = `http://localhost:5000/teach/${bookID}`
      axios.delete(path)
        .then(() => {
          this.getBooks()
          this.message = 'Teaching removed!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks()
        })
    },
    onDeleteBook(book) {
      this.removeBook(book.teacher_id)
    }
  }
}
</script>
