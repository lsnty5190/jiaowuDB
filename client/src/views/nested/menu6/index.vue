<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>TAKES</h1>
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
              <th scope="col">Student_ID</th>
              <th scope="col">Course_ID</th>
              <th scope="col">Sec_ID</th>
              <th scope="col">YEAR_SEMESTER</th>
              <th scope="col">Grade</th>
              <th />
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.student_id }}</td>
              <td>{{ book.course_id }}</td>
              <td>{{ book.sec_id }}</td>
              <td>{{ book.year_semester }}</td>
              <td>{{ book.grade }}</td>
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
      title="Add a new take"
      hide-footer
    >
      <b-form class="w-100" @submit="onSubmit" @reset="onReset">
        <b-form-group
          id="form-title-group"
          label="student_id:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="addBookForm.student_id"
            type="text"
            required
            placeholder="Enter Student_ID"
          />
        </b-form-group>
        
        <b-form-group
          id="form-ci-group"
          label="course_id:"
          label-for="form-ci-input"
        >
          <b-form-input
            id="form-ci-input"
            v-model="addBookForm.course_id"
            type="text"
            required
            placeholder="Enter Course_ID"
          />
        </b-form-group>

        <b-form-group
          id="form-si-group"
          label="sec_id:"
          label-for="form-si-input"
        >
          <b-form-input
            id="form-si-input"
            v-model="addBookForm.sec_id"
            type="text"
            required
            placeholder="Enter Stec_ID"
          />
        </b-form-group>

        <b-form-group
          id="form-ys-group"
          label="year semester:"
          label-for="form-ys-input"
        >
          <b-form-input
            id="form-ys-input"
            v-model="addBookForm.year_semester"
            type="text"
            required
            placeholder="Enter Year Semester"
          />
        </b-form-group>

        <b-form-group
          id="form-grade-group"
          label="Grade:"
          label-for="form-grade-input"
        >
          <b-form-input
            id="form-grade-input"
            v-model="addBookForm.grade"
            type="text"
            required
            placeholder="Enter Grade"
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
          label="student_id:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="editForm.student_id"
            type="text"
            required
            placeholder="Enter Student_ID"
          />
        </b-form-group>
        
        <b-form-group
          id="form-ci-group"
          label="course_id:"
          label-for="form-ci-input"
        >
          <b-form-input
            id="form-ci-input"
            v-model="editForm.course_id"
            type="text"
            required
            placeholder="Enter Course_ID"
          />
        </b-form-group>

        <b-form-group
          id="form-si-group"
          label="sec_id:"
          label-for="form-si-input"
        >
          <b-form-input
            id="form-si-input"
            v-model="editForm.sec_id"
            type="text"
            required
            placeholder="Enter Stec_ID"
          />
        </b-form-group>

        <b-form-group
          id="form-ys-group"
          label="year semester:"
          label-for="form-ys-input"
        >
          <b-form-input
            id="form-ys-input"
            v-model="editForm.year_semester"
            type="text"
            required
            placeholder="Enter Year Semester"
          />
        </b-form-group>

        <b-form-group
          id="form-grade-group"
          label="Grade:"
          label-for="form-grade-input"
        >
          <b-form-input
            id="form-grade-input"
            v-model="editForm.grade"
            type="text"
            required
            placeholder="Enter Grade"
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
          label="student_id:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="searchForm.student_id"
            type="text"
            required
            placeholder="Enter Student_ID"
          />
        </b-form-group>
        
        <b-form-group
          id="form-ci-group"
          label="course_id:"
          label-for="form-ci-input"
        >
          <b-form-input
            id="form-ci-input"
            v-model="searchForm.course_id"
            type="text"
            required
            placeholder="Enter Course_ID"
          />
        </b-form-group>

        <b-form-group
          id="form-si-group"
          label="sec_id:"
          label-for="form-si-input"
        >
          <b-form-input
            id="form-si-input"
            v-model="searchForm.sec_id"
            type="text"
            required
            placeholder="Enter Stec_ID"
          />
        </b-form-group>

        <b-form-group
          id="form-ys-group"
          label="year semester:"
          label-for="form-ys-input"
        >
          <b-form-input
            id="form-ys-input"
            v-model="searchForm.year_semester"
            type="text"
            required
            placeholder="Enter Year Semester"
          />
        </b-form-group>

        <b-form-group
          id="form-grade-group"
          label="Grade:"
          label-for="form-grade-input"
        >
          <b-form-input
            id="form-grade-input"
            v-model="searchForm.grade"
            type="text"
            required
            placeholder="Enter Grade"
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
        student_id: '',
        course_id: '',
        sec_id: '',
        year_semester: '',
        grade: ''
      },
      message: '',
      showMessage: false,
      editForm: {
        student_id: '',
        course_id: '',
        sec_id: '',
        year_semester: '',
        grade: ''
      },
      searchForm: {
        student_id: '',
        course_id: '',
        sec_id: '',
        year_semester: '',
        grade: ''
      }
    }
  },
  created() {
    this.getBooks()
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/takes'
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
      const path = 'http://localhost:5000/takes'
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
        const path = 'http://localhost:5000/takes/search'
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
      this.addBookForm.student_id = ''
      this.addBookForm.course_id = ''
      this.addBookForm.sec_id = ''
      this.addBookForm.year_semester = ''
      this.addBookForm.grade = ''

      this.editForm.student_id = ''
      this.editForm.course_id = ''
      this.editForm.sec_id = ''
      this.editForm.year_semester = ''
      this.editForm.grade = ''

      this.searchForm.student_id = ''
      this.searchForm.course_id = ''
      this.searchForm.sec_id = ''
      this.searchForm.year_semester = ''
      this.searchForm.grade = ''
    },
    onSubmit(evt) {
      evt.preventDefault()
      this.$refs.addBookModal.hide()
      // let read = false;
      // if (this.addBookForm.read[0]) read = true;
      const payload = {
        student_id: this.addBookForm.student_id,
        course_id: this.addBookForm.course_id,
        sec_id: this.addBookForm.sec_id,
        year_semester: this.addBookForm.year_semester,
        grade: this.addBookForm.grade
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
        student_id: this.searchForm.student_id,
        course_id: this.searchForm.course_id,
        sec_id: this.searchForm.sec_id,
        year_semester: this.searchForm.year_semester,
        grade: this.searchForm.grade
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
        student_id: this.editForm.student_id,
        course_id: this.editForm.course_id,
        sec_id: this.editForm.sec_id,
        year_semester: this.editForm.year_semester,
        grade: this.editForm.grade
      }
      this.updateBook(payload, this.editForm.student_id)
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/takes/${bookID}`
      axios.put(path, payload)
        .then(() => {
          this.getBooks()
          this.message = 'Student updated!'
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
      const path = `http://localhost:5000/takes/${bookID}`
      axios.delete(path)
        .then(() => {
          this.getBooks()
          this.message = 'Student removed!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks()
        })
    },
    onDeleteBook(book) {
      this.removeBook(book.student_id)
    }
  }
}
</script>
